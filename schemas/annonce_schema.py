import datetime
from pydantic import BaseModel, Field, ConfigDict  

class AnnonceBase(BaseModel):
    '''Schéma de données (ou modèle) créé avec la bibliothèque Pydantic.'''

    produit: str = Field(..., description="Le nom ou la description du produit")
    quantite: float = Field(..., description="La quantité du produit", gt=0)
    date: datetime.date = Field(..., description="La date de l'annonce (YYYY-MM-DD)")
    lat: float = Field(..., description="La latitude", ge=-90, le=90)
    long: float = Field(..., description="La longitude", ge=-180, le=180)

    # 2. Nouvelle syntaxe Pydantic V2 pour la configuration et l'exemple Swagger
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "produit": "Fraises",
                "quantite": 100.0,
                "date": "2026-10-05",
                "lat": 45.4783,
                "long": -75.7012
            }
        }
    )