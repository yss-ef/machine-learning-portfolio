from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Création du dataset sous forme de DataFrame
data = pd.DataFrame({
    'Heures': [1, 2, 6, 7],
    'Resultat': ['Echec', 'Echec', 'Reussite', 'Reussite']
})

print("Dataset :")
print(data)

# Séparation des caractéristiques (X) et de la cible (y)
X = data[['Heures']]
y = data['Resultat']

# Initialisation du modèle (Arbre de décision avec profondeur max de 1)
model = DecisionTreeClassifier(max_depth=1)

# Entraînement du modèle
model.fit(X, y)

# Prédiction pour une nouvelle donnée (5 heures)
nouvelle_donnee = pd.DataFrame({'Heures': [5]})
prediction = model.predict(nouvelle_donnee)

# Affichage du résultat
print("Prédiction pour 5 heures :", prediction[0])