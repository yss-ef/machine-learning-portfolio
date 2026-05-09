import pandas as pd
import numpy as np

def calculer_regression_matricielle(chemin_fichier_excel):
    try:
        # Étape 1 : Lecture des données
        donnees = pd.read_excel(chemin_fichier_excel, header=None)
        Y = donnees.iloc[:, 0].values.reshape(-1, 1)  # Vecteur colonne Y
        X_obs = donnees.iloc[:, 1].values.reshape(-1, 1) # Vecteur colonne X
        
        n = len(Y) # Nombre d'observations

        # Étape 2 : Construction de la matrice de design
        # On ajoute une colonne de 1 à gauche de nos observations X
        colonne_de_uns = np.ones((n, 1))
        X_design = np.hstack((X_obs, colonne_de_uns))

        print("Matrice Y:\n", Y)
        print("\nMatrice de Design (X_design):\n", X_design)

        # Étape 3 : Calculs matriciels avec l'équation normale
        # (X^T * X)
        XTX = X_design.T @ X_design
        
        # (X^T * X)^-1
        XTX_inv = np.linalg.inv(XTX)
        
        # X^T * Y
        XTY = X_design.T @ Y
        
        # beta = (X^T * X)^-1 * (X^T * Y)
        beta = XTX_inv @ XTY

        # Étape 4 : Extraction des coefficients
        a = beta[0][0]  # Pente
        b = beta[1][0]  # Ordonnée à l'origine

        return (b, a)

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier_excel}' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None



def calculer_erreur(chemin_fichier_excel, a, b):
    '''
     Calculer les erreures commises lors des calcules.
     '''

    try:
        donnees = pd.read_excel(chemin_fichier_excel, header=None)
        Y_reels = donnees.iloc[:, 0].values  # Y est la colonne 0
        X_obs = donnees.iloc[:, 1].values  # X est la colonne 1

        predictions = a * X_obs + b
        sse = np.sum((predictions - Y_reels) ** 2)
        return sse

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{chemin_fichier_excel}' n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None


# --- Utilisation de l'algorithme ---
# Créez un fichier excel nommé 'donnees_projet.xlsx' avec vos données
# ou remplacez le nom du fichier.
chemin_fichier = 'test.xlsx'
coefficients = calculer_regression_matricielle(chemin_fichier)

if coefficients:
    b, a = coefficients
    print(f"\n--- Résultats ---\n")
    print(f"L'ordonnée à l'origine (b) est : {b:.4f}")
    print(f"La pente (a) est : {a:.4f}")
    print(f"\nLe modèle de régression est : Y = {a:.4f}X + {b:.4f}")
    print(f"\nL'MSE de ce modele est : MSE = {calculer_erreur(chemin_fichier, a, b):.4f}")