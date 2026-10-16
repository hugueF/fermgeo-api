import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict  

class AnnonceBase(BaseModel):
    '''Schéma de données (ou modèle) créé avec la bibliothèque Pydantic.'''

    #... veut dire que le champ est obligatoire et doit être fourni lors de la création d'une instance du modèle.
    produit: str = Field(..., description="Le nom ou la description du produit") 
    quantite: float = Field(..., description="La quantité du produit", gt=0) #gt signifie que la valeur doit être strictement supérieure à 0
    date: datetime.date = Field(..., description="La date de l'annonce (YYYY-MM-DD)")
    lat: float = Field(..., description="La latitude", ge=-90, le=90) #ge signifie que la valeur doit être greater than or equal to -90
    long: float = Field(..., description="La longitude", ge=-180, le=180) #le signifie que la valeur doit être less than or equal to 180
    ville: str = Field(..., description="La ville ou se trouve le produit") 
    
    # 2. Nouvelle syntaxe Pydantic V2 pour la configuration et l'exemple Swagger
    #model_config est un dictionnaire de configuration qui permet de personnaliser le comportement du modèle Pydantic.
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "produit": "Fraises",
                "quantite": 100.0,
                "date": "2026-10-05",
                "lat": 45.4783,
                "long": -75.7012,
                "ville" : "Ottawa"
            }
        }
    )

# Modèle pour la mise a jour (hérite de TaskBase)
class AnnonceUpdate(BaseModel):
    ''' Mettre a jour un champ specifique'''
    quantite: Optional[float] = Field(None, gt=0)