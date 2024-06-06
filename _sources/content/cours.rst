Données structurées : les tables
================================

Stucture d'une table
---------------------
La manipulation de données en informatique nécessite de les structurer en faisant un choix adapté. La structure choisie doit permettre :

-   de modifier, ajouter, supprimer une donnée le plus simplement possible;
-   de pouvoir accéder rapidement à une donnée souhaitée;
-   éviter la redondance des données;
-   de conserver les données, les enregistrer pour les réutiliser.

Les ``tables`` sont une structure de données qui respectent ces contraintes. 

Une ``table`` est un ensemble de colonnes qui ont chacune un ``descripteur`` et de lignes qui sont les différents ``enregistrements`` contenant des valeurs pour chaque ``descripteur``.

.. figure:: ../img/table_1.png
    :align: center
    :width: 480

    Structure de table avec 3 enregistrements

.. admonition:: Application
    :class: application

    On souhaite créer une table sur des personnalités qui ont contribué au développement de l’informatique. On va utiliser les descripteurs suivants :

    .. table::
        :class: table bordure 

        +---+------+------------+---------+
        |nom|prénom|nationnalité|invention|
        +---+------+------------+---------+

    #.  Rechercher les informations sur ``Alan Turing``, ``John Conway`` et ``Ada Lovelace`` pour créer trois enregistrements.
    #.  Regrouper et organiser les données de ces trois enregistrements en utilisant un tableur.
    #.  Il existe des fichiers dont l’extension est **csv**.

        a.  Que signifie cette extension ? Quel est l’usage des fichiers **csv**.
        b.  Donner des applications qui permettent de créer un fichier **csv** ?

    #.  Enregistrer la table contenant les trois enregistrements dans un fichier ``table.csv``.
    #.  Ouvrir votre fichier ``table.csv`` avec le bloc-notes et vérifier la cohérence des données.
    #.  Ajouter dans le fichier ``table.csv`` ouvert avec le bloc-notes un enregistrement sur ``Guido von Rossum`` puis enregistrer.
    #.  Ouvrir le fichier ``table.csv`` avec un tableur et vérifier la présence de toutes les enregistrements.

Table en Python
-----------------

En python, une table se construit sous la forme d'une ``liste`` de ``dictionnaires``. 

-   Les ``descripteurs`` de la table sont les clés des dictionnaires. 
-   Il y a autant de dictionnaires que d'enregistrements.

Par exemple, la table de l'illustration précédente se code en Python de la façon suivante:

.. code:: python

    table = [
        {'descripteur 1':'valeur 1-1','descripteur 2': 'valeur 1-2', 'descripteur 3': 'valeur 1-3', 'descripteur 4': 'valeur 1-4'},
        {'descripteur 1':'valeur 2-1','descripteur 2': 'valeur 2-2', 'descripteur 3': 'valeur 2-3', 'descripteur 4': 'valeur 2-4'},
        {'descripteur 1':'valeur 3-1','descripteur 2': 'valeur 3-2', 'descripteur 3': 'valeur 3-3', 'descripteur 4': 'valeur 13-4'}
    ]

Comme Python est un langage de programmation, on manipule directement les données avec des scripts.

.. admonition:: Application
    :class: application
        
    #.  Créer en Python la table ``persinfo`` regroupant les enregistrements précédents.
    #.  Dans l’interpréteur ou un éditeur python, saisir les commandes pour:
        
        a. connaître le nombre d'enregistrements;
        b. récupérer les descripteurs de la table;
        c. récupérer les nationalités des enregistrements de la table;
        d. tester la présence de ``Turing`` dans la table;

    #.  Écrire une fonction ``chercher`` qui a pour paramètres la table et un descripteur et qui renvoie la liste de toutes les valeurs de la table associée à ce descripteur.

        Rechercher avec votre fonction tous les noms présents dans la table ``persinfo``.

    #.  Écrire une fonction ``est_present`` qui a pour paramètres une table et un enregistrement et qui vérifie la présence de cet enregistrement dans la table. La fonction ``est_present`` renvoie un booléen.

    #.  On souhaite créer une fonction ``ajouter`` qui ajoute un nouvel enregistrement dans la table si:

        -   l'enregistrement a bien les mêmes descripteurs;
        -   il y a au moins un nom, les autres valeurs peuvent être vides;
        -   l'enregistrement n'est pas déjà dans la table.

        a.  Écrire la fonction ``ajouter`` qui a pour paramètres la table et un dictionnaire enregistrement. 
        b.  Ajouter avec votre fonction l'enregistrement de ``Guido von Rossum``.
        c.  Tester votre fonction avec des enregistrements particuliers :  vide, déjà présent, sans nom.


Python et fichier csv
-----------------------

Un programme Python peut utiliser des données provenant d'un fichier structuré comme le csv. Une fois chargé, la table est enregistrée dans une variable en étant transformée en liste de dictionnaires.

Cette transformation des données se réalise avec le module ``csv`` qui permet :

-   de récupérer les données contenues dans un fichier ``csv`` sous forme de table;
-   d'ajouter, enregistrer les données d'une table python dans un fichier ``csv``.

L'accès aux données contenues dans un fichier csv se fait avec la commande ``with open``. Elle prend différents paramètres :

-   le nom du fichier avec le chemin d’accès;
-   le mode d’accès: ``mode='r'`` pour lire un contenu, ``mode='w'`` pour écrire un contenu et ``mode='a'`` pour ajouter du contenu;
-   l'encodage de caractères du fichier à lire : ``encoding='utf8'``
-   l'ajout d'une ligne vide pour l'écriture: ``newline=''``
-   en fin de ligne on utilise la commande ``as`` pour créer un alias du nom de fichier ouvert.

.. code:: python
    :caption: Python

    with open(fichier, mode = 'r', encoding = 'utf8') as f:

.. admonition:: Application
    :class: application

    #.  Importer le module csv de python : ``import csv``
    #.  Pour lire le contenu d’un fichier csv, on crée la fonction suivante :

        .. code:: python

            def lire_fichier(fichier):
                with open(fichier,mode='r',encoding='utf8') as f:
                    data=csv.DictReader(f)
                    table=[]
                    for ligne in data:
                        table.append(dict(ligne))
                    f.close()
                return table

        Ajouter cette fonction à votre fichier.

    #.  Quel est l'appel qui permet de lire le contenu de votre fichier ``table.csv`` ?
    #.  Quel est le type de la variable table renvoyée par la fonction ?
    #. Créer la variable ``table`` qui est une table dont le contenu est celui du fichier ``table.csv``.

    #.  Ajouter à la variable les personnalités **Guido von Rossum** et **Tim Berners-Lee**.

    #.  Pour écrire dans un fichier, on crée la fonction suivante:

        .. code:: python

            def ecrire_fichier(fichier,table):
                clefs=list(table[0].keys())
                with open(fichier,mode='w',encoding='utf8',newline='') as f:
                    data = csv.DictWriter(f,clefs)
                    data.writeheader()
                    data.writerows(table)
                    f.close()

        Ajouter cette fonction à votre fichier.

    #.  Écrire le contenu de votre variable ``table`` dans un fichier ``table2.csv``.

    #.  On va écrire un programme principal qui:

        -   lit le contenu d’un fichier csv contenant des personnalités du monde informatique;
        -   propose l'ajout de nouvelles personnalités dans la table;
        -   enregistre dans le même fichier la table et ses nouvelles fiches à la fin de la saisie.
