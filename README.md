# Projet Brute Force en Python
## Description
Ce projet a pour but de réaliser un programme en Python qui permet de tester la force d'un mot de passe en utilisant la méthode de la force brute pour mon parcours de certification.

## Logiciels utilisés
- Python 3.9.6
- PyCharm
- pip
- Git
- GitHub
# detail comme si tu le presentais a un client
## Installation
Pour installer le programme, il suffit de cloner le projet sur votre machine en utilisant la commande suivante:
```bash
git clone
```
Ensuite, il faut installer les dépendances du projet en utilisant la commande suivante:
```bash
pip install -r requirements.txt
```
## Utilisation
Pour utiliser le programme, il suffit de lancer le fichier main.py en utilisant la commande suivante:
```bash
python main.py
```
# liste les dependances utilisees dans le projet
## Dépendances
- itertools
- threading
- time
- requests
- tkinter
- os
- ctypes

N'oubliez pas de créer un fichier `Dockerfile` dans votre projet pour que les instructions Docker fonctionnent correctement. Voici un exemple de `Dockerfile` :

```dockerfile
# Utiliser une image de base Python
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Définir la commande par défaut
CMD ["python", "main.py"]

Ensuite, il suffit de suivre les instructions affichées dans la console pour tester la force d'un mot de passe.
## Auteur
- Nom: Bouzac
- Prénom: Ludovic
