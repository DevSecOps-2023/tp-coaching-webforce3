FROM python:3.6.1-alpine

# Définition du répertoire de travail
WORKDIR /app
# Installation des dépendances Python
COPY ./requirements.txt /app/requirements.txt
RUN pip install  --no-cache-dir ca-r requirements.txt
# Copie des fichiers de l'application dans le conteneur
COPY ../blogs.py /app
# Exposition du port 5000 pour l'application Flask
 EXPOSE 30102
ENTRYPOINT FLASK_APP=/app/blogs.py flask run --host=0.0.0.0
