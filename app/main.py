import sys
from pathlib import Path
# Ajoute automatiquement le dossier parent (dossier_principal) au système
sys.path.append(str(Path(__file__).resolve().parents[1]))
from fastapi import FastAPI
from routes.annonce_route import router as annonce_routeur
#Importe le routeur  situé dans le dossier routes et le fichier 
#annonce_route.py. Le mot-clé as annonce_router est un alias pour renommer localement 
#la variable router afin d'éviter toute confusion si nous importons d'autres routeurs plutard 

app = FastAPI()
#variable app devient le point central du projet. 
#C'est elle qui va recevoir toutes les requêtes HTTP des utilisateurs, 
#gérer la configuration globale et générer la documentation automatique (/docs).

app.include_router(annonce_routeur)