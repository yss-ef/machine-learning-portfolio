import pandas as pd
import matplotlib.pyplot as plt

# Étape 1 : Lecture des données
try:
    # Charger le fichier Excel
    df = pd.read_excel('test.xlsx', header=None)
    # Assigner les colonnes comme tu l'as demandé : Y est la première, X la seconde.
    Y = df[0]
    X = df[1]
except FileNotFoundError:
    print("Erreur : Le fichier 'donnees.xlsx' n'a pas été trouvé.")
    print("Assure-toi que le fichier est dans le même dossier que le script.")
    exit()

# Étape 2 : Initialisation des paramètres
# On commence avec une droite y = 0x + 0
m = 0.0
b = 0.0

# Hyperparamètres de l'algorithme
learning_rate = 0.01  # Le "pas" que l'on fait à chaque itération
iterations = 1000  # Le nombre de fois où on répète le calcul

n = float(len(X))  # Nombre de points de données

# Pour stocker l'historique de l'erreur et la visualiser plus tard
cost_history = []

# Étape 3 : Algorithme de la Descente du Gradient
print("Début de l'entraînement...")
for i in range(iterations):
    # Calculer les prédictions actuelles Y = mX + b
    Y_pred = m * X + b

    # Calculer le coût (Erreur Quadratique Moyenne) pour cette itération
    cost = (1 / n) * sum([val ** 2 for val in (Y - Y_pred)])
    cost_history.append(cost)

    # Calculer les gradients (les dérivées partielles)
    gradient_m = (-2 / n) * sum(X * (Y - Y_pred))
    gradient_b = (-2 / n) * sum(Y - Y_pred)

    # Mettre à jour les paramètres m et b
    m = m - learning_rate * gradient_m
    b = b - learning_rate * gradient_b

    # Afficher la progression de temps en temps
    if i % 100 == 0:
        print(f"Itération {i}: m = {m:.4f}, b = {b:.4f}, Erreur = {cost:.4f}")

print("\nEntraînement terminé !")
print(f"Résultat final : m = {m:.4f}, b = {b:.4f}")
print(f"Équation de la droite : Y = {m:.2f}X + {b:.2f}")
