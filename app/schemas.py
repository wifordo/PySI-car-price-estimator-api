from pydantic import BaseModel, Field

"""
    Schemat wejściowy z walidacją typów danych (Pydantic).
    Aliasy zapewniają zgodność z nazewnictwem w pliku Excel.
"""
class CarInput(BaseModel):
    # Przepisanie pół z nauczonego modelu na aliasy by nie używać w kodzie polskich znaków i spacji
    rok_produkcji: int = Field(..., alias="Rok produkcji", gt=1900)
    przebieg: int = Field(..., alias="Przebieg w km", ge=0)
    moc: int = Field(..., alias="Moc w KM", ge=0)
    euro: int = Field(..., alias="Norma spalin Euro")

    class Config:
        populate_by_name = True

class PredictionOutput(BaseModel):
    estimated_price_pln: float