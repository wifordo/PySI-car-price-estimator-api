# API do Estymacji/szacowania Ceny Samochodów Używanych

## 1. Cel projektu
Projekt realizuje zadanie budowy lokalnego systemu AI as a Service. Model przewiduje cenę rynkową samochodu na podstawie danych historycznych (zapisanych w pliku auta.xlsx na bazie którego nauczono model). 
Projekt jest skalowalny, dzięki takiej modułowości - dane historyczne są przechowywane w pliku Excel, co pozwala na łatwe dotrenowanie modelu bez konieczności modyfikacji kodu źródłowego. Dzięki temu łatwo jest wytrenować nowy model nie ruszając kodu. 

## 2. Architektura i Proces
1. **Trening**: Skrypt `train/train.py` wczytuje dane z `train/auta.xlsx`, trenuje model regresji liniowej i zapisuje go do `model/car_model.joblib`.
2. **Serwer**: Aplikacja FastAPI wczytuje gotowy model przy starcie i udostępnia endpoint do predykcji.
3. **Dane**: Model uwzględnia: Rok produkcji, Przebieg (km), Moc (KM) oraz Normę spalin Euro.

## 3. Instalacja i uruchomienie

### Opcja A: Przez narzędzie `uv` 
1. Synchronizacja środowiska:
   ```bash
   uv sync
   
2. Uruchomienie serwera:
- Uruchomienie standardowe: `uvicorn app.main:app`
- Uruchomienie w trybie deweloperskim (z automatycznym odświeżaniem kodu): `uvicorn app.main:app --reload`

### Opcja B: Przez standardowe pip
1. Instalacja: `pip install -r requirements.txt`
- 2a. Uruchomienie standardowe: `uvicorn app.main:app`
- 2b. Uruchomienie w trybie deweloperskim (z automatycznym odświeżaniem kodu): `uvicorn app.main:app --reload`

## 4. Dokumentacja API
Po uruchomieniu serwera, interaktywna dokumentacja Swagger UI dostępna jest pod adresem:
- http://127.0.0.1:8000/docs

## 5. Instrukcja użycia

Opis endpointów

    GET /: Powitanie i status serwera.

    POST /predict: Główny endpoint służący do wyceny auta.

    GET /docs: Interaktywna dokumentacja Swagger UI.

Przykład zapytania (JSON)
Aby przetestować model, należy wysłać zapytanie typu POST z danymi w formacie JSON. Nazwy pól muszą być zgodne z nagłówkami użytymi w pliku Excel:

```json
{
  "Rok produkcji": 2020,
  "Przebieg w km": 45000,
  "Moc w KM": 150,
  "Norma spalin Euro": 6
}

Przykładowa odpowiedź

{
  "estimated_price_pln": 102448.52
}
```
## 6. Informacje o modelu i danych
Użyty model

System wykorzystuje model Regresji Liniowej (LinearRegression) z biblioteki scikit-learn. Model został wytrenowany lokalnie na zbiorze danych z pliku auta.xlsx, a następnie zapisany do formatu .joblib w celu szybkiego ładowania przez API.

Model przyjmuje cztery cechy numeryczne (Dane wejściowe):

- Rok produkcji (liczba całkowita)

- Przebieg w km (liczba całkowita)

- Moc w KM (liczba całkowita)

- Norma spalin Euro (liczba całkowita od 4 do 6)
*Uwaga: W przypadku podnorm (np. 6d, 6temp), należy wprowadzić główny numer normy (6).*
Dane wyjściowe
- Cena w PLN: Przewidywana wartość rynkowa (liczba zmiennoprzecinkowa).

## 7. Autorzy
- Dawid Wikar