import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# data
data = pd.DataFrame({
    'Age' : [22, 25, 47, 52],
    'Revenu' : [2500, 3000, 9000, 11000],
    'Premium' : [0, 0, 1, 1]
})

# separation variables
x = data[['Age', 'Revenu']]
y = data[['Premium']]

# creation et entainement du module
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)

# nouveau client
nouveau_client = pd.DataFrame([[30, 4000]], columns=['Age', 'Revenu'])
prediction = model.predict(nouveau_client)
print("Prediction pour (30, 4000): )", prediction[0])

