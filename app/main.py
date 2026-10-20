import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
# Ajoute automatiquement le dossier parent (dossier_principal) au système
sys.path.append(str(Path(__file__).resolve().parents[1]))
from routes.annonce_route import router as annonce_routeur
#Importe le routeur  situé dans le dossier routes et le fichier 
#annonce_route.py. Le mot-clé as annonce_router est un alias pour renommer localement 
#la variable router afin d'éviter toute confusion si nous importons d'autres routeurs plutard 
from app.database import Base, engine
from fastapi.staticfiles import StaticFiles #Importe la classe StaticFiles de FastAPI pour servir des fichiers statiques (CSS, JS, images, etc.) à partir d'un répertoire spécifique.

app = FastAPI()
#variable app devient le point central du projet. 
#C'est elle qui va recevoir toutes les requêtes HTTP des utilisateurs, 
#gérer la configuration globale et générer la documentation automatique (/docs).

# Création des tables au démarrage
Base.metadata.create_all(bind=engine)

app.include_router(annonce_routeur)

FRONTEND_DIR = Path(__file__).resolve().parents[1] / "frontend" #permet de définir le chemin vers le dossier frontend, qui contient les fichiers HTML, CSS et JavaScript de l'interface utilisateur.


@app.get("/", include_in_schema=False) #permet de définir une route pour la page d'accueil de l'application.
async def homepage():
    return FileResponse(FRONTEND_DIR / "homepage.html")

@app.get("/publier.html", include_in_schema=False) #permet de définir une route pour la page de publication des annonces.
async def page_publication():
    return FileResponse(FRONTEND_DIR / "publier.html")

app.mount("/frontend", StaticFiles(directory=FRONTEND_DIR), name="frontend") #permet de monter le répertoire frontend pour servir les fichiers statiques (CSS, JS, images, etc.) à partir de ce répertoire. Cela signifie que les fichiers situés dans le dossier frontend seront accessibles via l'URL /frontend.
app.mount("/CSS",StaticFiles(directory="frontend/CSS"),name="css")
app.mount("/Javascript",StaticFiles(directory="frontend/Javascript"),name="javascript")
app.mount("/frontend",StaticFiles(directory="frontend/Javascript"),name="")
