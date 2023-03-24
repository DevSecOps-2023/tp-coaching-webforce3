Voici un exemple de Dockerfile qui permet de créer une image Docker avec Ubuntu, Python, Flask et tous les packages nécessaires pour exécuter une application Flask Web :

Dockerfile
Copy code
# Utilisation de l'image de base Ubuntu
FROM ubuntu:latest

# Installation des paquets nécessaires
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de l'application dans le conteneur
COPY . /app

# Installation des dépendances Python
RUN pip3 install -r requirements.txt

# Exposition du port 5000 pour l'application Flask
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["python3", "app.py"]
Assurez-vous d'avoir un fichier requirements.txt dans le même répertoire que le Dockerfile, contenant la liste des packages Python nécessaires pour votre application Flask. Vous pouvez également modifier le port exposé (EXPOSE) et la commande pour lancer l'application (CMD) en fonction de votre application.

Ensuite, pour construire l'image Docker à partir de ce Dockerfile, vous pouvez exécuter la commande suivante dans le même répertoire que votre Dockerfile :

bash
Copy code
docker build -t nom_image_docker .
Cela va construire une nouvelle image Docker nommée nom_image_docker à partir du Dockerfile. Enfin, vous pouvez exécuter le conteneur à partir de l'image en utilisant la commande suivante :

bash
Copy code
docker run -p 5000:5000 nom_image_docker
Cela va exécuter le conteneur à partir de l'image Docker créée précédemment et le lier au port 5000 de votre ordinateur local. Vous devriez maintenant pouvoir accéder à votre application Flask via un navigateur Web en visitant l'URL http://localhost:5000.