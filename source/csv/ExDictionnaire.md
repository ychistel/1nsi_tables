<span>Exercice</span><span>Dictionnaire en Python</span>

Exercice  {#exercice .unnumbered}
---------

1.  Créer un dictionnaire europe avec au moins 8 éléments et respectant
    la structure suivante :

    -   Les clés seront des pays européens;

    -   Les valeurs seront les capitales de ces pays.

2.  La fonction **len** permet de connaître le nombre d’éléments.
    Vérifier que votre dictionnaire a 8 éléments.

3.  Ajouter par une simple affectation la “Pologne” et sa capitale
    “Varsovie”.

4.  Ajouter par affectation le pays dont la capitale est Riga.

5.  Ajouter par une affectation la Finlande.

6.  Ajouter la Hongrie et sa capitale “Bucarest” (c’est une erreur
    volontaire), puis modifier avec la bonne capitale hongroise. Ajouter
    le pays dont la capitale est “Bucarest”.

7.  Combien avez-vous de valeurs dans votre dictionnaire ?

8.  Afficher à l’aide de 2 boucles les clés puis les valeurs de
    votre dictionnaire.

Exercice  {#exercice-1 .unnumbered}
---------

On va créer un dictionnaire pour afficher une fiche identité de
célébrités.

1.  Créer un dictionnaire **célébrités** ayant la structure suivante :

    -   Les clés du dictionnaire sont des personnalités célèbres (noms);

    -   Les valeurs sont des tableaux contenant dans l’ordre : la
        nationalité, l’année de naissance, l’année de décès et leur
        activité professionnelle.

    Par exemple : **zidane** est la clé pour les valeurs
    \[’france’,’1972’,”,football’\]

2.  Créer plusieurs entrées dans votre dictionnaire au moins trois.

3.  Créer une fonction **saisir** qui permet d’ajouter des célébrités à
    votre dictionnaire en saisissant les valeurs dans des **input**
    (voir ci-dessous).

    ![image](img/celebrite1.eps)

    Saisissez avec votre fonction 3 nouvelles célébrités et vérifiez que
    le dictionnaire est bien structuré.

    ![image](img/celebrite2.eps)

4.  Créer une fonction **pays** qui prend en paramètre le dictionnaire
    et une clé du dictionnaire et retourne le pays d’origine de la
    célébrité (voir ci-dessous).

    ![image](img/celebrite3.eps)

5.  Créer de même la fonction **naissance** qui retourne l’année de
    naissance de la célébrité.

6.  Créer de même une fonction **vivant** qui retourne une valeur
    booléenne (True, False) et vérifie si la célébrité est
    toujours vivante.

    ![image](img/celebrite4.eps)

7.  Écrire une fonction **age** qui donne l’âge de la célébrité.
    Attention, les années saisies sont des chaines de caractères, donc
    pour effectuer les calculs, il faut les convertir en “integer” avec
    la fonction **eval**.

8.  Créer la fonction **activité** qui retourne l’activité de
    la célébrité.

9.  Écrire une fonction **cle\_de\_valeur** qui liste toutes les
    célébrités (clés) qui ont une valeur commune. Par exemple, la même
    nationalité, la même année de naissance ou la même activité.

    ![image](img/celebrite5.eps)

10. Créer une fonction **identité** qui liste toutes les informations
    sur la célébrité se trouvant dans le dictionnaire. La fonction
    retournera un texte sur plusieurs lignes.

    ![image](img/celebrite6.eps)

11. Pour finir, écrire un programme qui prend en saisie une valeur à
    chercher dans le dictionnaire et qui affiche toutes les valeurs
    (ou clés) trouvées en concordance.

    ![image](img/celebrite7.eps)

12. Pour aller plus loin, on traitera aussi les cas ou rien n’est trouvé
    et également en prenant compte de la syntaxe utilisée (majuscules
    ou non).

13. Améliorer le code pour gérer les éventuelles erreurs dues à une
    mauvaise saisie.

Exercice  {#exercice-2 .unnumbered}
---------

Dans l’exercice précédent, on a utilisé un unique dictionnaire pour
enregistrer dans une même variable différentes célébrités.

![image](img/listedico1.eps)

-   Le nom de la célébrité est utilisée en tant que clé de dictionnaire;

-   La valeur associée à chaque clé est un tableau contenant la
    nationalité, la date de naissance, la date de décès et l’activité de
    la célébrité.

On peut organiser ces données dans une structure différente. On la donne
ci-dessous :

![image](img/listedico3.eps)

1.  Quelle est la nouvelle structure utilisée ?

2.  Quelle instruction python affiche le nom de la première célébrité ?
    et la seconde célébrité ?

3.  Écrire une boucle qui affiche tous les noms des célébrités.

    Transformer cette boucle en une fonction **nom** qui renvoie la
    liste des noms de toutes les célébrités.

    ![image](img/listedico4.eps)

4.  Écrire une fonction python **pratique** qui renvoie les **noms** des
    célébrités qui pratiquent un sport donné. La fonction prendra en
    paramètre la variable **célébrités** et le **sport** demandé.

    ![image](img/listedico5.eps)

5.  Écrire une fonction python **ma\_célébrité** qui renvoie l’ensemble
    des données d’une célébrité pour un **nom** donné. La fonction
    prendra en paramètres la variable **célébrités** et le
    **nom** demandé.

    ![image](img/listedico6.eps)

6.  Modifier les fonctions **age** et **identité** de l’exercice
    précédent pour qu’elles s’appliquent avec la nouvelle structure de
    la variable **célébrités**.

7.  Écrire un programme qui prend en saisie une valeur à chercher dans
    la variable célébrités et affiche toutes les valeurs trouvées en
    concordance avec la célébrité.

    ![image](img/listedico7.eps)

Exercice  {#exercice-3 .unnumbered}
---------

1.  Créer les listes suivantes (vous pouvez modifier les valeurs mais
    pas leur nombre) :

    ![image](img/dicoliste1.eps)

2.  Écrire une fonction **aleadico** qui renvoie un dictionnaire dont
    les clés sont **nom**, **couleur** et **instrument** et dont les
    valeurs sont choisies aléatoirement parmi les trois listes noms,
    couleurs et instruments.

    La fonction prendra comme paramètres **n**, **c** et **i**
    correspondant aux les 3 listes noms, couleurs et instruments.

    ![image](img/dicoliste2.eps)

3.  Écrire une fonction **listedicos** qui renvoie une liste (tableau)
    contenant plusieurs dictionnaires créés par la fonction aleadico. Le
    nombre de dictionnaire à créer sera défini par le paramètre **n** de
    la fonction.

4.  Créer une liste contenant 20 dictionnaires aléatoires et affecter la
    valeur à la variable **t**.

    ![image](img/dicoliste3.eps)

5.  Écrire une fonction qui cherche si deux dictionnaires au moins sont
    identiques, c’est à dire avec le même nom, la même couleur et le
    même instrument de musique.

    ![image](img/dicoliste4.eps)

6.  Écrire une fonction qui renvoie le nom le plus fréquent dans
    le dictionnaire. Il peut y en avoir plusieurs !

    ![image](img/dicoliste5.eps)

    Faire de même avec la couleur et l’instrument.
