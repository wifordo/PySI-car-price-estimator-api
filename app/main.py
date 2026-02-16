from fastapi import FastAPI
import joblib
import numpy as np
import os
from app.schemas import CarInput, PredictionOutput

app = FastAPI(title="System Wyceny Aut")

# Wczytujemy model przy starcie serwera (tylko raz)
MODEL_PATH = os.path.join("model", "car_model.joblib")
model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"status": "Serwer działa", "docs": "/docs"} # Zwrotka że serwer działa


@app.post("/predict", response_model=PredictionOutput)
def predict_price(car: CarInput):
    # Przygotowanie danych do predykcji
    data = np.array([[car.rok_produkcji, car.przebieg, car.moc, car.euro]])

    # Wykonanie predykcji
    prediction = model.predict(data)

    return {"estimated_price_pln": round(float(prediction[0]), 2)}