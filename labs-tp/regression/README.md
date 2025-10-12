# 📈 Projet de Régression Linéaire Simple

Ce projet a été réalisé dans le cadre du module d'**Analyse des Données Multidimensionnelles**. Il présente deux approches pour calculer les coefficients d'un modèle de régression linéaire simple ($Y = aX + b$) à partir de données fournies dans un fichier Excel.

1.  **Méthode 1 : Descente du Gradient (Approche Itérative)**
2.  **Méthode 2 : Équation Normale (Approche Matricielle)**

---
---

## Méthode 1 : Descente du Gradient (Approche Itérative)

Cette première approche utilise la **descente du gradient**, un algorithme d'optimisation qui minimise l'erreur quadratique moyenne de manière itérative pour trouver les meilleurs coefficients.

### ✨ Fonctionnalités

-   **Lecture de données** depuis un fichier Excel (`.xlsx`).
-   **Calcul itératif** des coefficients : la pente `a` et l'ordonnée à l'origine `b`.
-   **Visualisation des résultats** avec Matplotlib, montrant la droite de régression et la courbe de diminution de l'erreur.
-   **Paramètres ajustables** comme le taux d'apprentissage et le nombre d'itérations.

### ✅ Prérequis

-   **Pandas** : Pour la lecture et la manipulation des données.
-   **Matplotlib** : Pour la visualisation des graphiques.

Vous pouvez les installer avec la commande suivante :
```bash
pip install pandas matplotlib openpyxl
```
### 🧠 Explication de la Méthode

La descente du gradient cherche à trouver le minimum d'une fonction (ici, la fonction d'erreur) en suivant la direction de la pente la plus forte. Tel un randonneur cherchant le point le plus bas d'une vallée dans le brouillard, il procède par petits pas successifs. La mise à jour des coefficients se fait à chaque itération jusqu'à ce qu'ils convergent vers les valeurs optimales.

---

## Méthode 2 : Équation Normale (Approche Matricielle)

Cette seconde approche utilise la méthode des moindres carrés via l'équation normale, qui s'appuie sur des opérations d'algèbre linéaire (matrices) pour trouver une solution directe et analytique.

### ✨ Fonctionnalités

* Lecture de données depuis un fichier Excel (`.xlsx`).

* Calcul automatique des coefficients de la régression : la pente `a` et l'ordonnée à l'origine `b`.

* Implémentation pure de la formule matricielle sans utiliser de bibliothèques de machine learning comme Scikit-learn.

* Affichage clair du modèle de régression final.

### ✅ Prérequis

* **Pandas** : Pour la lecture et la manipulation des données.

* **NumPy** : Pour les calculs numériques et matriciels.

Vous pouvez les installer avec la commande suivante :
```Bash
pip install pandas numpy openpyxl
```

### 🚀 Comment l'utiliser ?

1. 📝 Préparez votre fichier de données :

   * Créez un fichier Excel (par exemple, donnees.xlsx).

   * La première colonne doit contenir vos données pour la variable dépendante (Y).

   * La deuxième colonne doit contenir vos données pour la variable indépendante (X).

   * Le fichier ne doit pas contenir d'en-têtes.

2. 🔧 Modifiez le nom du fichier dans le script :

   * Ouvrez le fichier de script Python.

   * Modifiez la ligne chemin_fichier = 'donnees_projet.xlsx' pour indiquer le chemin de votre propre fichier.
  
3. ▶️ Exécutez le script :

   * Ouvrez un terminal dans le dossier du projet et lancez la commande suivante :
     ```Bash
     python ModRegression-1.py
     ```
4. 👀 Consultez les résultats :
    * Le script affichera la pente (a) et l'ordonnée à l'origine (b) calculées, ainsi que l'équation finale de votre modèle.
  
### 🧠 Explication de la Méthode

Le calcul est basé sur l'équation normale, qui fournit une solution analytique au problème des moindres carrés. La formule est la suivante :

$$\hat{\beta} = (X^T X)^{-1} X^T Y$$

Où :

* $\hat{\beta} est le vecteur contenant les coefficients `b` (intercept) et `a` (pente).
* Y est le vecteur des valeurs de la variable dépendante.
* X est la matrice de design, composée d'une colonne de 1 (pour l'intercept) et d'une colonne avec les valeurs de la variable indépendante.

