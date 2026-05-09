import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Valeur de base
data = pd.DataFrame({
    'Age': [25, 45, np.nan, 50, 23, 40],
    'Revenu': [3000, 8000, 5000, np.nan, 2500, 7000],
    'Frequence_achat': [1, 5, 3, 6, 1, 4],
    'Ville': ['Rabat', 'Casablanca', 'Rabat', 'Fes', 'Fes', 'Casablanca'],
    'client_premium': [0, 1, 0, 1, 0, 1]
})
print(data)
print('---------------------------------------------------------------------')

# Remplissage des valeurs NA
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Revenu'] = data['Revenu'].fillna(data['Revenu'].mean())

print(data)
print('---------------------------------------------------------------------')

# separation des villes
data_encoded = pd.get_dummies(data, columns=['Ville'], dtype=int)

print(data_encoded)
print('---------------------------------------------------------------------')

# Separation des variables
x = data_encoded.drop(columns=['client_premium'])
y = data_encoded['client_premium']

# Colonnes numerique a normaliser
num_cols = ['Age', 'Revenu', 'Frequence_achat']

# init scaler
scaler = StandardScaler()

# Application du scaling uniq sur les colonnes numerique
x[num_cols] = scaler.fit_transform(x[num_cols])

print(x)
print('---------------------------------------------------------------------')

