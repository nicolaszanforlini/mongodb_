# Simplon-DD2-unittest-pymongo
Les tests unitaires en python et l'utilisation de pymongo

## Installation
1. *forker* ce dépôt
2. cloner le dépôt *forké* sur votre machine
3. sur votre machine, créer une base mongoDB nommée *unittest_pymongo*
4. dans cette base, créer les collections *films* et *actors*
5. exécuter le script python *fill_films.py* (long temps d'exécution) puis vérifier que la collection *films* est remplie de documents

## Le site Movie DB
1. lancer le script *imdb_flask.py*
2. sur votre navigateur, ouvrir l'URL *localhost:5000*

On voit que le nombre de films et d'acteurs est à 0.

Pour avoir le bon nombre de films, modifier la méthode *get_nb_films* de la classe *Film* dans *MongoDB.py* pour qu'elle retourne le bon nombre de films.

## Tests unitaires

**Test unitaire** de la modification de la méthode *get_nb_films* :

1. lancer le script *unittests.py* : le résultat indique une erreur
2. modifier le script *unittests.py* pour que le test unitaire ne renvoie pas d'erreur

## Acteurs
Il faut maintenant remplir la collection *actors* de la base *unittest_pymongo*.

1. modifier la méthode *get_actors* de la classe *Film* dans *MongoDB.py* pour qu'elle retourne la liste d'acteurs d'un film.
2. ajouter un test unitaire de cette méthode dans *unittests.py* qui sera exécuté pour vérification 
3. en s'inspirant du script *fill_films.py*, créer le script *fill_actors* pour remplir la collection *actors*. **Attention !** : en regardant bien dans la collection *films*, on voit que les noms d'acteurs d'un film sont "sales" : les nettoyer avant de charger la collection *actors*.
4. modifier la méthode *get_nb_actors* de la classe *Actor* dans *MongoDB.py* pour qu'elle retourne le bon nombre d'acteurs.
5. ajouter un test unitaire dans *unittests.py* pour vérifier la dernière modification (créer une nouvelle classe nommée *TestFilmMethods*.

## Pendant ce temps là, moi je...
...fais en sorte d'enrichir le site pour qu'il soit plus pro

## Rappelez-vous !
1. Réussir c'est bien, apprendre c'est mieux !
2. s'entraider comme dans une équipe de dev en entreprise, communiquer !
3. écrire sa réflexion avant de coder.
