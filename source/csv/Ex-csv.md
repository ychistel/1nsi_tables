<span>Exercice</span><span>Fichier CSV - Données en table</span>

Exercice  {#exercice .unnumbered}
---------

Travailler les données d’une table d’un fichier csv sous forme de liste.

1.  Récupérer le fichier MEC.csv listant les meilleures entrées au
    cinéma depuis 1945 en France et le téléverser sur le serveur JUPYTER
    dans un dossier **csv**.

2.  Éditer le fichier et identifier le délimiteur utilisé pour séparer
    les champs.

3.  Recopier les instructions python ci-dessous dans une cellule d’un
    notebook Jupyter.

    ![image](img/Excsv2.eps)

    Contrôler que votre affichage ressemble à la capture suivante:

    ![image](img/Excsv1.eps)

4.  1.  Afficher le nombre de films américains présents dans la table.

    2.  Afficher les titres des films français.

    3.  Afficher le film classé 25 dans la table.

5.  Écrire une fonction **film\_par\_pays** qui renvoie une liste
    contenant les titres de tous les films issus du même pays. Le
    paramètre **pays** sera demandé.

6.  La variable **table** contient les données sous forme de liste mais
    n’est pas simple à manipuler. Pour simplifier, on va créer une
    **liste de liste de films** avec la fonction **list**.

    Remplacer l’instruction table=csv.reader(f,delimiter=“;”) par
    table=list(csv.reader(f,delimiter=“;”)).

7.  Avec la nouvelle valeur attibuée à la variable **table** :

    1.  Afficher le nombre de films américains présents dans la table.

    2.  Afficher les titres des films français.

    3.  Afficher le film classé 25 dans la table.

Exercice  {#exercice-1 .unnumbered}
---------

Travailler les données d’une table d’un fichier csv sous forme de
dictionnaire.

1.  Recopier les instructions python ci-dessous dans une cellule d’un
    notebook Jupyter.

    ![image](img/Excsv3.eps)

    Contrôler que votre affichage ressemble à la capture suivante:

    ![image](img/Excsv4.eps)

2.  1.  Afficher le nombre de films américains présents dans la table.

    2.  Afficher les titres des films français.

    3.  Afficher le film classé 25 dans la table.

3.  Écrire une fonction **film\_par\_pays** qui renvoie une liste
    contenant les titres de tous les films issus du même pays. Le
    paramètre **pays** sera demandé.

4.  Écrire une fonction **film\_par\_année** qui prend en paramètre la
    table et une année et renvoie un résultat si l’année est trouvée et
    undictionnaire vide si l’année n’est pas trouvée.

5.  Vérifier s’il existe un film pour l’année 2019. On pourrait chercher
    à intégrer un film dans la table. Quelles sont les modifications
    qu’il faudrait effectuer ?

Exercice  {#exercice-2 .unnumbered}
---------

1.  Soit **voyage** une variable définie comme sur la capture
    ci-dessous:

    ![image](img/Excsv5.eps)

    Créer cette variable dans un notebook Jupyter.

2.  Écrire dans un fichier de type csv, le contenu de cette table. On
    utilisera les fonctions python du module csv. Le fichier sera nommé
    **voyage.csv** et sera enregistré dans le dossier **csv**
    du serveur.

3.  Ajouter une entrée supplémentaire dans la variable voyage avec la
    fonction **append**, puis enregistrer à nouveau la table dans le
    fichier csv.

4.  Écrire une fonction **saisir\_voyage** qui permet de saisir la ville
    de départ, la ville d’arrivée, la distance en km et la durée du
    séjour et l’ajoute comme entrée dans la varible voyage.

5.  Écrire une fonction **enregistre** qui écrit la table das le
    fichier csv. La fonction prendra en paramètre le nom du fichier et
    la table à enregistrer.

6.  Que fait la fonction donnée ci-dessous:

    ![image](img/Excsv6.eps)

7.  Recopier et compléter la boucle **while** pour saisir et erngistrer
    de nouveaux voyages dans la table et dans le fichier voyage.csv:

    ![image](img/Excsv7.eps)

    Vérifier votre code en réalisant des saisies et en vérifiant votre
    fichier csv.

Exercice  {#exercice-3 .unnumbered}
---------

Reprise de l’exercice 4 du fichier **ExDictionnaire** dans lequel on
crée une table contenant des dictionnaires créés aléatoirement.

1.  Écrire un code qui permet d’enregistrer la table dans un fichier
    **dicoalea.csv**.

2.  Écrire un code qui permet d’ajouter les réponses aux
    questions posées.
