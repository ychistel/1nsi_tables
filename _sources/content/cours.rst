Structure de données en tables
==============================

La manipulation de données en informatique nécessite de les structurer en faisant un choix adapté. La structure choisie doit permettre :

-   de modifier, ajouter, supprimer une donnée le plus simplement possible;
-   de pouvoir accéder rapidement à une donnée souhaitée;
-   éviter la redondance des données;
-   de conserver les données, les enregistrer pour les réutiliser.

La liste n’est pas exhaustive, d’autres actions sont possibles.

Il existe une structure de donnée qui permet de respecter cet ensemble de contraintes et se présente sous forme de tables.

On va réaliser une table de données regroupant des informations sur des personnalités qui ont contribué au développement de l’informatique. On va utiliser le modèle de fiche suivant:

.. container:: center

   +--------------+
   | nom:         |
   +--------------+
   | prénom:      |
   +--------------+
   | nationalité: |
   +--------------+
   | invention:   |
   +--------------+

Créer trois fiches sur **Alan Turing**, **John Conway** et **Ada Lovelace** en effectuant les recherches sur wikipedia.

Une première table
-------------------

#.  Regrouper et organiser les données de ces trois fiches dans un même tableau.
#.  Il existe des fichiers dont l’extension est **csv**.

    a.  Que signifie cette extension ? Quel est l’usage des fichiers **csv**.
    b.  Donner des applications qui permettent de créer un fichier **csv** ?

#.  Dans un tableur, saisissez les données des trois fiches puis enregistrer les données dans un fichier ``table.csv`` avec l’extension csv.

#.  Ouvrir votre fichier ``table.csv`` avec le bloc-notes et vérifier la cohérence des données, leur présentation.

#. Ajouter dans le fichier ``table.csv`` ouvert avec le bloc-notes la fiche de ``Guido von Rossum`` puis enregistrer.

#. Ouvrir le fichier ``table.csv`` avec un tableur et vérifier la présence de toutes les fiches.

Table en Python
-----------------

En python, une table peut se construire sous la forme d’une **liste** de **dictionnaires**. Comme Python est un langage de programmation, il permet de manipuler directement les données avec des scripts.

#.  Écrire en Python la table ``persinfo`` regroupant les trois fiches. Chaque fiche est un dictionnaire et la table est la liste de ces dictionnaires.

#.  Dans l’interpréteur ou un éditeur python, saisir les commandes pour:
    
    a. connaître le nombre de fiches;
    b. récupérer les clefs des fiches de la table;
    c. récupérer les nationalités des fiches de la table;
    d. tester la présence de Turing dans la table;

#.  Écrire une fonction ``chercher`` qui a pour paramètres la table et une clef du dictionnaire (fiche) et qui renvoie la liste de toutes les valeurs de la table associée à cette clef. On effectuera un test d’existence de la clef !

#.  Rechercher avec votre fonction tous les noms présents dans la table.

#.  Écrire une fonction ``est_present`` qui a pour paramètres une table et une fiche dictionnaire et vérifie la présence de la fiche dans la table. La fonction renvoie ``True`` si la fiche est dans la table, ``False`` sinon.

#.  On souhaite créer une fonction ``ajouter_fiche`` qui ajoute une fiche dans la table si:

    -   la fiche a bien les mêmes clefs;
    -   il y a au moins un nom, les autres valeurs peuvent être vides;
    -   la fiche n’est pas déjà dans la table.

    a.  Écrire la fonction qui a pour paramètres la table et un dictionnaire fiche. 
    b.  Ajouter avec votre fonction la fiche de Guido von Rossum.
    c.  Tester votre fonction avec des cas particuliers : fiche vide, fiche déjà présente, fiche sans nom.

#.  Créer une fonction ``saisir_fiche`` qui permet d'ajouter des fiches dans la table avec des ``input``.

Python et fichier csv
-----------------------

Il ne pas confondre les variables avec les données. Un programme s’écrit avec des variables qui vont stocker des données. Ces données peuvent être définies dans le programme, calculées par le programme, etc. 

Les données peuvent être saisies par l’utilisateur du programme. Un programme peut utiliser des données provenant d’un fichier structuré comme le csv.

Il existe en Python un module ``csv`` qui permet :

-   de récupérer les données contenues dans un fichier ``csv`` sous forme de table;
-   d'ajouter, enregistrer les données d’une table python dans un fichier ``csv``.

L’accès aux données contenues dans un fichier csv se fait avec la commande ``with open``. Elle prend différents paramètres :

-   le nom du fichier csv avec le chemin d’accès;
-   le mode d’accès: ``mode='r'`` pour lire un contenu, ``mode='w'`` pour écrire un contenu et ``mode='a'`` pour ajouter du contenu;
-   l'encodage de caractères du fichier à lire : ``encoding='utf8'``
-   l'ajout d'une ligne vide pour l'écriture: ``newline=''``

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
