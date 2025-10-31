import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

userData = pd.read_csv("../Datos/UserData.csv")

X = userData[['Age']].values
y = userData['EstimatedSalary'].values

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'api/modelo_lineal.pkl')

print("Modelo de regresion lineal simple creado")
print(f"Coeficiente: {model.coef_[0]:.2f}")
print(f"Interseccion: {model.intercept_:.2f}")
print("Predice salario estimado basado en la edad")
