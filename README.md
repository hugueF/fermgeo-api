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

## Liens utiles
- L'API en direct : http://127.0.0.1:8000/health
- La documentation interactive : http://127.0.0.1:8000/docs