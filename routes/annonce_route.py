import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from fastapi import APIRouter, Depends
# Import de la session SQLAlchemy (connexion à SQLite)
from app.database import SessionLocal
# Import du modèle ORM Annonce (table SQLite)
from app.models import Annonce
# Import du schéma Pydantic (structure des données reçues/envoyées)
from schemas.annonce_schema import AnnonceBase
from sqlalchemy.orm import Session

router = APIRouter(prefix="/annonces", tags=["Annonces"])
#Permet de classer cette section sous la catégorie "Annonces" 
#dans la documentation interactive générée automatiquement par FastAPI (/docs)'''

# Dépendance permettant d'obtenir une session de base de données pour chaque requête
def get_db():
    """
    Ouvre une session vers la base SQLite.
    La session est fermée automatiquement après la requête.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AnnonceBase)
async def creer_annonce(annonce: AnnonceBase, db: Session = Depends(get_db)):
    """
    Crée une nouvelle annonce dans la base SQLite via SQLAlchemy.

    - `annonce`: données reçues depuis le client (schéma Pydantic)
    - `db`: session SQLAlchemy injectée automatiquement grâce à Depends(get_db)
    """

    # Conversion du schéma Pydantic en modèle ORM (objet SQLAlchemy)
    annonce_sql = Annonce(
        produit=annonce.produit,
        quantite=annonce.quantite,
        lat=annonce.lat,
        long=annonce.long,
        date =annonce.date
    )

    # Ajout de l'annonce dans la base de données
    db.add(annonce_sql)

    # Validation de l'opération (écriture dans le fichier SQLite)
    db.commit()

    # Recharge l'objet depuis la base pour récupérer les champs générés (ex: id auto-incrémenté)
    db.refresh(annonce_sql)

    # Retourne l'annonce créée (FastAPI convertit automatiquement en AnnonceBase)
    return annonce_sql


@router.get("/", response_model=list[AnnonceBase])
async def lire_annonces(produit: str | None = None, db: Session = Depends(get_db)):
    """
    Récupère toutes les annonces depuis la base SQLite.
    Permet un filtrage optionnel par produit via un paramètre de requête.

    - Si `produit` est fourni, on filtre les annonces correspondantes.
    - Sinon, on retourne toutes les annonces.
    """

    # Construction de la requête SQLAlchemy
    query = db.query(Annonce)

    # Filtrage par produit si un paramètre est fourni
    if produit:
        # ilike = comparaison insensible à la casse (équivalent de lower() == lower())
        query = query.filter(Annonce.produit.ilike(produit))

    # Exécution de la requête et récupération des résultats
    return query.all()