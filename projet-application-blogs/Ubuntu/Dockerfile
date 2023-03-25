# Utilisation de l'image de base Ubuntu
# FROM ubuntu:latest
FROM ubuntu:20.04
# Installation des paquets nécessaires
RUN apt-get update 
RUN apt-get -y install python3 python3-pip vim iputils-ping
#&& apt-get install -y \
#    python3 python3-pip vim && \
 #   pip3 install flask \  
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

# Définition du répertoire de travail
WORKDIR /app
# Installation des dépendances Python
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
# Copie des fichiers de l'application dans le conteneur
COPY ../blogs.py /app


# Exposition du port 5000 pour l'application Flask
 EXPOSE 30101

# Commande pour lancer l'application Flask
# ENTRYPOINT [ "python3" ]
 #CMD ["blogs.py"]
ENTRYPOINT FLASK_APP=/app/blogs.py flask run --host=0.0.0.0
