import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import warnings
warnings.filterwarnings("ignore")

userData = pd.read_csv("../Datos/UserData.csv")

x = userData.iloc[:,[2,3]].values
y = userData.iloc[:,4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

st_x = StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)

clf = LogisticRegression()
clf.fit(x_train, y_train)

joblib.dump(clf, 'api/modelo_regresion_logistica.pkl')
joblib.dump(st_x, 'api/scaler.pkl')

print("Modelo de regresion logistica creado")
print("Archivos guardados:")
print("- api/modelo_regresion_logistica.pkl")
print("- api/scaler.pkl")
