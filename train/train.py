import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression # <-- Użycie regresji
import joblib
import os

# 1. Wczytujemy dane
try:
    df = pd.read_excel('train/auta.xlsx')
    print("Dane załadowane pomyślnie!")
except Exception as e:
    print(f"Błąd: {e}")
    exit()

# 2. Mapujemy dane tj. dane z excela do zmiennych x i y
X = df[['Rok produkcji', 'Przebieg w km', 'Moc w KM', 'Norma spalin Euro']]
y = df['Cena w PLN']

# 3. Trenujemy model
model = LinearRegression()
model.fit(X, y)

# 3. Zapisujemy w folderze model/
os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/car_model.joblib')

print("Model auta zapisany w folderze model/!")