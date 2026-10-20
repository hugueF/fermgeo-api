# fermgeo-api
FastAPI backend and interactive map for real-time local harvest discovery in Ottawa-Gatineau.

## Installation
Pour installer les outils nécessaires :
```bash
pip install fastapi uvicorn
```

## Lancer le serveur local
Pour démarrer le serveur en mode développement :
```bash
uvicorn app.main:app --reload
```
Ouvrez ensuite la page d'accueil à l'adresse http://127.0.0.1:8000/. Elle charge les annonces depuis l'API `/annonces/`; gardez le serveur démarré pendant la navigation.

## Liens utiles
- L'API en direct : http://127.0.0.1:8000/health
- La documentation interactive : http://127.0.0.1:8000/docs