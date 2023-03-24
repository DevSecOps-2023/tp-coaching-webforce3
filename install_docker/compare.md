ansible fait maison 

Mettre à jour tous les packages de la machine avec la commande apt.
Installer les paquets requis pour le bon fonctionnement de Docker, tels que apt-transport-https, ca-certificates, curl, gnupg-agent, software-properties-common, python3-pip, python3-venv et ansible.
Ajouter la clé GPG officielle de Docker à la liste des clés connues de la machine.
Ajouter le référentiel Docker à la liste des sources apt de la machine.
Mettre à jour à nouveau tous les packages de la machine.
Installer les packages Docker, notamment docker-ce, docker-ce-cli et containerd.io.
Ajouter l'utilisateur actuel (ubuntu) au groupe Docker pour éviter d'utiliser sudo chaque fois que Docker est utilisé.
Installer le package Python docker via pip pour une utilisation facile de l'API Docker en Python.


chatgpt

Mettre à jour tous les packages de la machine avec la commande apt.
Installer les paquets requis pour le bon fonctionnement de Docker, tels que apt-transport-https, ca-certificates, curl, gnupg-agent, software-properties-common, python3-pip, python3-venv et ansible.
Ajouter la clé GPG officielle de Docker à la liste des clés connues de la machine.
Ajouter le référentiel Docker à la liste des sources apt de la machine.
Mettre à jour à nouveau tous les packages de la machine.
Installer les packages Docker, notamment docker-ce, docker-ce-cli et containerd.io.
Ajouter l'utilisateur actuel (ubuntu) au groupe Docker pour éviter d'utiliser sudo chaque fois que Docker est utilisé.
Installer le package Python docker via pip pour une utilisation facile de l'API Docker en Python.



fait zd

La première tâche installe les dépendances requises pour Docker (apt-transport-https, ca-certificates, curl, gnupg-agent, software-properties-common) en utilisant le module apt.
La deuxième tâche ajoute la clé GPG de Docker à l'hôte en utilisant le module apt_key.
La troisième tâche ajoute le référentiel Docker à la liste des sources de paquets de l'hôte en utilisant le module apt_repository.
La quatrième tâche installe les packages Docker (docker-ce, docker-ce-cli, containerd.io) en utilisant le module apt.
La cinquième tâche s'assure que le service Docker est en cours d'exécution et qu'il démarre automatiquement au démarrage de l'hôte en utilisant le module service.
Un gestionnaire est également défini pour redémarrer le service Docker en cas de changements de configuration.