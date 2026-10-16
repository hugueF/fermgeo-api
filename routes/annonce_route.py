import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from fastapi import APIRouter, Depends
from app.database import SessionLocal # Import de la session SQLAlchemy (connexion à SQLite)
from app.models import Annonce # Import du modèle ORM Annonce (table SQLite)
from schemas.annonce_schema import AnnonceBase, AnnonceUpdate# Import du schéma Pydantic (structure des données reçues/envoyées)
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

#Permet de classer cette section sous la catégorie "Annonces" 
#dans la documentation interactive générée automatiquement par FastAPI (/docs)'''
router = APIRouter(prefix="/annonces", tags=["Annonces"])

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

    - 'annonce': données reçues depuis le client (schéma Pydantic)
    - 'db': session SQLAlchemy injectée automatiquement grâce à Depends(get_db)
    """

    # Conversion du schéma Pydantic en modèle ORM (objet SQLAlchemy)
    annonce_sql = Annonce(
        produit=annonce.produit,
        quantite=annonce.quantite,
        lat=annonce.lat,
        long=annonce.long,
        date =annonce.date,
        ville = annonce.ville
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

    - Si 'produit' est fourni, on filtre les annonces correspondantes.
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

#Cette route est utilisée pour mettre a jour le statut ou le titre d une annonce precise. 
@router.patch("/annonces/{annonce_id}")
async def mise_a_jour_annonce(annonce_id: int, annonce_update: AnnonceUpdate, db: Session = Depends(get_db)):
    # Recherche de l annonce
    annonce = db.query(Annonce).filter(Annonce.id == annonce_id).first()

    if annonce is None:
        raise HTTPException(status_code=404,detail="Annonce introuvable")

    # Récupère uniquement les champs envoyés
    update_data = annonce_update.model_dump(exclude_unset=True)

    # Mise à jour des champs fournis
    for key, value in update_data.items():
        setattr(annonce, key, value)

    db.commit()
    db.refresh(annonce)

    return annonce

#Cette route est utilisée pour msupprimer une tache precise. 
@router.delete("/{annonce_id}", status_code=status.HTTP_200_OK)
async def suppression_annonce(annonce_id: int, db: Session = Depends(get_db)):
    # Recherche de l annonce
    annonce = db.query(Annonce).filter(Annonce.id == annonce_id).first()

    if annonce is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"L annonce avec l'id {annonce_id} n'existe pas."
        )

    # Suppression
    db.delete(annonce)
    db.commit()

    return {
        "message": f"L'annonce dont l'id est {annonce_id} a été supprimée avec succès."
    }