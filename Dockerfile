#image Python
FROM python:3.9-slim

#répertoire de travail
WORKDIR /app

#pour copier les fichiers
COPY . .

#dépendances
RUN pip install --no-cache-dir -r requirements.txt

#commande pour démarrer FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

