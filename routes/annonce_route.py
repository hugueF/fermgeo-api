import sys
from pathlib import Path
# Ajoute automatiquement le dossier parent (dossier_principal) au système
sys.path.append(str(Path(__file__).resolve().parents[1]))
# L'import fonctionne maintenant de partout
from schemas.annonce_schema import AnnonceBase 
from fastapi import APIRouter 

router = APIRouter(prefix="/annonces", tags=["Annonces"])
#Permet de classer cette section sous la catégorie "Annonces" 
#dans la documentation interactive générée automatiquement par FastAPI (/docs)'''

@router.post("/")
async def creer_annonce(annonce: AnnonceBase):

    '''Déclare une fonction asynchrone, ce qui permet à FastAPI 
    de gérer un grand nombre de requêtes simultanées de manière très efficace.'''

    return {"message": "Succès", "donnees": annonce.model_dump()}
#annonce.model_dump() : C'est une méthode de Pydantic (v2) qui convertit l'objet Python annonce 
# en un dictionnaire standard (clé/valeur), ce qui permet d'inclure toutes les données de l'annonce 
# reçue dans la réponse finale.