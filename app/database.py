from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de la base SQLite (dans la racine du projet)
DATABASE_URL = "sqlite:///./database_fermgeo.db"

# Création du moteur
engine = create_engine(DATABASE_URL, echo=True)

# Session pour les opérations CRUD
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base ORM
class Base(DeclarativeBase):
    pass