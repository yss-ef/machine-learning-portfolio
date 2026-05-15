from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import json
import os
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.svm import SVR, SVC
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score, roc_auc_score,
    mean_squared_error, mean_absolute_error, r2_score,
    confusion_matrix, classification_report
)

app = Flask(__name__)

DATA_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS = {
    "mat": os.path.join(DATA_DIR, "data", "student-mat.csv"),
    "por": os.path.join(DATA_DIR, "data", "student-por.csv"),
}

# ─── helpers ──────────────────────────────────────────────────────────────────

def load_and_clean(dataset_key, target_mode, selected_features=None):
    df = pd.read_csv(DATASETS[dataset_key])

    # ── cleaning report
    cleaning_log = []
    cleaning_log.append(f"Loaded {len(df)} rows, {len(df.columns)} columns")
    cleaning_log.append(f"Missing values: {df.isnull().sum().sum()}")
    dupes = df.duplicated().sum()
    if dupes > 0:
        df.drop_duplicates(inplace=True)
        cleaning_log.append(f"Removed {dupes} duplicate rows → {len(df)} remaining")
    else:
        cleaning_log.append("No duplicate rows found")

    # ── build target
    if target_mode == "G3_reg":
        y = df["G3"].values
        task = "regression"
    elif target_mode == "pass_class":
        y = (df["G3"] >= 10).astype(int).values
        task = "classification"
    elif target_mode == "grade_class":
        bins = pd.cut(df["G3"], bins=[-1, 9, 13, 20], labels=["fail", "medium", "high"])
        le = LabelEncoder()
        y = le.fit_transform(bins)
        task = "multiclass"
    else:
        raise ValueError("Unknown target mode")

    # ── feature set
    drop_cols = ["G3", "G1", "G2"] if target_mode in ["pass_class", "grade_class"] else ["G3"]
    # keep G1, G2 for regression
    if target_mode == "G3_reg":
        drop_cols = ["G3"]

    feature_df = df.drop(columns=drop_cols, errors="ignore")

    # binary yes/no
    binary_cols = [c for c in feature_df.columns if set(feature_df[c].dropna().unique()).issubset({"yes","no"})]
    for c in binary_cols:
        feature_df[c] = (feature_df[c] == "yes").astype(int)
    cleaning_log.append(f"Binary-encoded {len(binary_cols)} yes/no columns: {', '.join(binary_cols)}")

    # one-hot
    cat_cols = feature_df.select_dtypes(include="object").columns.tolist()
    feature_df = pd.get_dummies(feature_df, columns=cat_cols, drop_first=True)
    cleaning_log.append(f"One-hot encoded {len(cat_cols)} categorical columns: {', '.join(cat_cols)}")

    all_features = feature_df.columns.tolist()

    if selected_features:
        # map original names → encoded columns
        kept = [c for c in all_features if any(c == f or c.startswith(f+"_") for f in selected_features)]
        feature_df = feature_df[kept]
    
    cleaning_log.append(f"Final feature matrix: {feature_df.shape[0]} rows × {feature_df.shape[1]} columns")

    X = feature_df.values
    feature_names = feature_df.columns.tolist()

    # scale
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    cleaning_log.append("Applied StandardScaler to all numeric features")

    return X_scaled, y, feature_names, task, cleaning_log, df


def get_model(model_key, task, seed=42):
    models = {
        "lr": {
            "regression": LinearRegression(),
            "classification": LogisticRegression(max_iter=500, random_state=seed),
            "multiclass": LogisticRegression(max_iter=500, random_state=seed),
        },
        "ridge": {
            "regression": Ridge(alpha=1.0),
            "classification": LogisticRegression(C=0.5, max_iter=500, random_state=seed),
            "multiclass": LogisticRegression(C=0.5, max_iter=500, random_state=seed),
        },
        "dt": {
            "regression": DecisionTreeRegressor(max_depth=5, random_state=seed),
            "classification": DecisionTreeClassifier(max_depth=5, random_state=seed),
            "multiclass": DecisionTreeClassifier(max_depth=5, random_state=seed),
        },
        "rf": {
            "regression": RandomForestRegressor(n_estimators=100, max_depth=6, random_state=seed),
            "classification": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=seed),
            "multiclass": RandomForestClassifier(n_estimators=100, max_depth=6, random_state=seed),
        },
        "gb": {
            "regression": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=seed),
            "classification": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=seed),
            "multiclass": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=seed),
        },
        "knn": {
            "regression": KNeighborsRegressor(n_neighbors=5),
            "classification": KNeighborsClassifier(n_neighbors=5),
            "multiclass": KNeighborsClassifier(n_neighbors=5),
        },
        "svm": {
            "regression": SVR(kernel="rbf", C=1.0),
            "classification": SVC(kernel="rbf", probability=True, random_state=seed),
            "multiclass": SVC(kernel="rbf", probability=True, random_state=seed),
        },
    }
    return models[model_key][task]


def compute_feature_importance(model, feature_names, X_train, y_train, task):
    try:
        if hasattr(model, "feature_importances_"):
            imp = model.feature_importances_
        elif hasattr(model, "coef_"):
            coef = model.coef_
            imp = np.abs(coef).mean(axis=0) if coef.ndim > 1 else np.abs(coef)
        else:
            return []

        pairs = sorted(zip(feature_names, imp.tolist()), key=lambda x: -x[1])
        total = sum(v for _, v in pairs) or 1
        return [{"feature": f, "importance": round(v/total, 4)} for f, v in pairs[:15]]
    except Exception:
        return []


# ─── routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/dataset-info", methods=["GET"])
def dataset_info():
    infos = {}
    for key, path in DATASETS.items():
        df = pd.read_csv(path)
        infos[key] = {
            "rows": len(df),
            "cols": len(df.columns),
            "columns": df.columns.tolist(),
            "numeric_cols": df.select_dtypes(include="number").columns.tolist(),
            "cat_cols": df.select_dtypes(include="object").columns.tolist(),
            "missing": int(df.isnull().sum().sum()),
            "g3_mean": round(df["G3"].mean(), 2),
            "g3_std": round(df["G3"].std(), 2),
            "pass_rate": round((df["G3"] >= 10).mean() * 100, 1),
            "g3_dist": df["G3"].value_counts().sort_index().to_dict(),
        }
    return jsonify(infos)


@app.route("/api/eda", methods=["POST"])
def eda():
    data = request.json
    dataset_key = data.get("dataset", "mat")
    df = pd.read_csv(DATASETS[dataset_key])

    numeric = df.select_dtypes(include="number")
    corr = numeric.corr()["G3"].drop("G3").sort_values(ascending=False)

    # grade distribution
    g3_counts = df["G3"].value_counts().sort_index()

    # failures breakdown
    fail_g3 = df.groupby("failures")["G3"].mean().round(2).to_dict()

    # studytime vs G3
    study_g3 = df.groupby("studytime")["G3"].mean().round(2).to_dict()

    return jsonify({
        "correlations": {k: round(v, 4) for k, v in corr.items()},
        "g3_distribution": {int(k): int(v) for k, v in g3_counts.items()},
        "failures_vs_g3": {int(k): float(v) for k, v in fail_g3.items()},
        "studytime_vs_g3": {int(k): float(v) for k, v in study_g3.items()},
        "sex_pass": df.groupby("sex").apply(lambda x: round((x["G3"]>=10).mean()*100, 1)).to_dict(),
        "address_g3": df.groupby("address")["G3"].mean().round(2).to_dict(),
    })


@app.route("/api/train", methods=["POST"])
def train():
    data = request.json
    dataset_key = data.get("dataset", "mat")
    target_mode = data.get("target", "G3_reg")
    selected_models = data.get("models", ["lr", "dt", "rf", "gb"])
    selected_features = data.get("features", None)
    cv_folds = int(data.get("cv_folds", 5))
    seed = int(data.get("seed", 42))
    test_size = float(data.get("test_size", 0.2))

    try:
        X, y, feature_names, task, cleaning_log, df_orig = load_and_clean(
            dataset_key, target_mode, selected_features
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed
    )

    results = []
    for model_key in selected_models:
        try:
            model = get_model(model_key, task, seed)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            if task == "regression":
                rmse = float(np.sqrt(mean_squared_error(y_test, y_pred)))
                mae = float(mean_absolute_error(y_test, y_pred))
                r2 = float(r2_score(y_test, y_pred))
                cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="r2")
                metrics = {
                    "rmse": round(rmse, 4),
                    "mae": round(mae, 4),
                    "r2": round(r2, 4),
                    "cv_r2_mean": round(cv_scores.mean(), 4),
                    "cv_r2_std": round(cv_scores.std(), 4),
                }
                primary = r2
                primary_label = "R²"
            else:
                acc = float(accuracy_score(y_test, y_pred))
                f1 = float(f1_score(y_test, y_pred, average="weighted"))
                prec = float(precision_score(y_test, y_pred, average="weighted", zero_division=0))
                rec = float(recall_score(y_test, y_pred, average="weighted", zero_division=0))
                cv_scores = cross_val_score(model, X, y, cv=cv_folds, scoring="accuracy")
                cm = confusion_matrix(y_test, y_pred).tolist()
                try:
                    if task == "classification":
                        y_prob = model.predict_proba(X_test)[:, 1]
                        auc = round(float(roc_auc_score(y_test, y_prob)), 4)
                    else:
                        auc = None
                except Exception:
                    auc = None
                metrics = {
                    "accuracy": round(acc, 4),
                    "f1": round(f1, 4),
                    "precision": round(prec, 4),
                    "recall": round(rec, 4),
                    "auc": auc,
                    "cv_acc_mean": round(cv_scores.mean(), 4),
                    "cv_acc_std": round(cv_scores.std(), 4),
                    "confusion_matrix": cm,
                }
                primary = acc
                primary_label = "Accuracy"

            fi = compute_feature_importance(model, feature_names, X_train, y_train, task)

            results.append({
                "model_key": model_key,
                "metrics": metrics,
                "feature_importance": fi,
                "primary": round(primary, 4),
                "primary_label": primary_label,
            })

        except Exception as e:
            results.append({"model_key": model_key, "error": str(e)})

    # sort best first
    valid = [r for r in results if "error" not in r]
    if task == "regression":
        valid.sort(key=lambda r: -r["metrics"].get("r2", -99))
    else:
        valid.sort(key=lambda r: -r["metrics"].get("accuracy", 0))

    return jsonify({
        "task": task,
        "dataset": dataset_key,
        "target": target_mode,
        "n_train": len(X_train),
        "n_test": len(X_test),
        "n_features": len(feature_names),
        "cleaning_log": cleaning_log,
        "results": valid + [r for r in results if "error" in r],
    })


if __name__ == "__main__":
    print("\n🚀  Student ML Platform running → http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)
