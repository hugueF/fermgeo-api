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

ANNONCE_DB: list[AnnonceBase] = [] #permet de stocker les annonces créées dans une liste en mémoire.

@router.post("/", response_model=AnnonceBase)# permet de créer une nouvelle annonce en utilisant la méthode POST.
async def creer_annonce(annonce: AnnonceBase):
    """
    Crée une annonce et l'ajoute à la base en mémoire.
    """
    ANNONCE_DB.append(annonce) # Ajoute l'annonce reçue à la liste ANNONCE_DB, qui sert de base de données en mémoire pour stocker les annonces.
    return annonce

@router.get("/", response_model=list[AnnonceBase]) #permet de récupérer toutes les annonces en utilisant la méthode GET.
async def lire_annonces(produit: str | None = None): # permet de filtrer les annonces par produit si un paramètre de requête "produit" est fourni. Si aucun produit n'est spécifié, toutes les annonces sont retournées.
    """
    Lit les annonces avec filtrage simple par produit.
    """
    if produit: # Si un produit est spécifié dans la requête, on filtre les annonces pour ne retourner que celles correspondant au produit demandé.
        return [
            annonce
            for annonce in ANNONCE_DB
            if annonce.produit.lower() == produit.lower() #Ignore la casse lors de la comparaison des produits
        ]
    return ANNONCE_DB