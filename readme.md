# Générateur de Codes QR - MouhaTech

## Description

Ce projet est une application web Django simple pour générer des codes QR. Les utilisateurs peuvent saisir des données (comme une URL) et optionnellement télécharger un logo pour l'intégrer dans le code QR généré.

## Fonctionnalités

- Génération de codes QR à partir de données textuelles
- Intégration optionnelle d'un logo dans le code QR
- Stockage des codes QR générés dans la base de données pour un accès ultérieur
- Interface web simple pour l'utilisation

## Prérequis

````bash
- Python 3.8 ou supérieur
- Django 5.2
- qrcode 8.2
- Pillow 12.0
- django-environ 0.12
````

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone <url-du-dépôt>
   cd qrcode
   ```

2. Créez un environnement virtuel :

   ```bash
   python -m venv env
   env\Scripts\activate  # Sur Windows
   source env/bin/activate # Sur macOS/Linux
   ```

3. Installez les dépendances :

   ```bash
   pip install -r src/requirements.txt
   ```

4. Appliquez les migrations :

   ```bash
   cd src
   python manage.py migrate
   ```

5. Créez un fichier `.env` dans le dossier `Generator` avec les variables d'environnement nécessaires :
   ```bash
   SECRET_KEY=votre-clé-secrète
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

## Utilisation

1. Lancez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

2. Ouvrez votre navigateur et allez à `http://127.0.0.1:8000/`

3. Saisissez l'URL ou les données pour le code QR
4. Téléchargez un logo optionnel (format image)
5. Cliquez sur "Générer" pour créer le code QR

## Structure du Projet

- `src/dj_qr/` : Configuration principale de Django
- `src/Generator/` : Application Django pour la génération de QR codes
  - `models.py` : Modèle QR_code
  - `views.py` : Vue pour la génération et l'affichage
  - `templates/` : Templates HTML
  - `static/` : Fichiers statiques
- `media/` : Stockage des images générées

## Contribution

Les contributions sont les bienvenues ! Veuillez créer une issue ou une pull request.

## Auteur

Ce projet est développé par Mouhamed Mbaye, développeur web full-stack. Voir son portfolio sur [MouhaTech](https://mouhatech.com).

## Licence

Ce projet est distribué sous licence MIT.  
Vous êtes libre de l’utiliser, le modifier et le redistribuer.