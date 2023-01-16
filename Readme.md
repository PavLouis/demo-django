# Quickstart avec Django

## Files:

### ```manage.py```

Fichier script qui facilite l'exécution de certaines tâches courantes dans le projet.

##### Les commandes à savoir

``` python manage.py runserver ``` démarre un serveur web local pour tester  l'application.

``` python manage.py startapp name ``` : crée une nouvelle application dans un projet Django.

``` python manage.py makemigrations ``` : crée les fichiers de migration pour les modèles de votre application.
( Un fichier de migration est un fichier généré par Django, qui décrit les modifications à apporter à la base de données pour synchroniser les modèles de votre application avec celle-ci. )

``` python manage.py migrate ```  : exécute les migrations pour mettre à jour la base de données en fonction de vos modèles.

``` python manage.py createsuperuser ```  : crée un nouvel utilisateur administrateur pour votre application.

``` python manage.py test name```  : exécute les tests unitaires pour votre application.

### ```settings.py```

Fichier de config qui contient les paramètres de config de votre projet.

##### Les variables intéressantes

``` INSTALLED_APPS ``` : Il contient une liste des applications installées dans votre projet.

``` DATABASES ``` : Il contient les paramètres de config de la base de données pour votre projet, comme le type de base de données (par exemple, MySQL ou PostgreSQL), l'hôte, le nom d'utilisateur et le mot de passe, etc.


### ```views.py```

Fichier qui contient les vues (fonctions/classes qui gèrent les requêtes HTTP et renvoient les réponses appropriées) de l'application. Généralement utilisées pour gérer les interactions avec les modèles (et les templates). Situé dans le dossier de chaque application de votre projet.

### ```urls.py```
Fichier qui contient les configs des URL pour l'application. Permet de définir les URL de  l'application et de les relier aux vues appropriées.

### ```models.py```
Fichier qui contient les modèles de l'application. Ils décrivent les données de l'application, comme les tables dans une base de données relationnelle.