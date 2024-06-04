import csv

# On définit notre table persinfo
persinfo=list()
persinfo.append({'nom':'turing','prénom':'alan','nationalité':'anglaise','invention':'machine de turing'})
persinfo.append({'nom':'lovelace','prénom':'ada','nationalité':'anglaise','invention':'premier programme informatique'})
persinfo.append({'nom':'conway','prénom':'john','nationalité':'anglaise','invention':'jeu de la vie'})

def chercher(table,clef):
    valeurs=list()
    for dico in table:
        if clef in dico.keys():
            valeurs.append(dico[clef])
    return valeurs

def est_present(table,fiche):
    k=0
    while k < len(table):
        if table[k]==fiche:
            return True
        else:
            k+=1
    return False

def ajouter_fiche(table,fiche):
    if fiche!={} and fiche.keys()==table[0].keys() and fiche['nom']!='' and not est_present(table,fiche):
        table.append(fiche)
    
def saisir_fiche(table):
    while True:
        rep=input("Saisir une nouvelle fiche ? (o/n)")
        if rep=='o' or rep=='O':
            fiche=dict()
            for clef in table[0].keys():
                fiche[clef]=input('Saisir le/la '+clef+" : ")
            ajouter_fiche(table,fiche)
        else:
            break

def ecrire_fichier(fichier,table):
    clefs=list(table[0].keys())
    with open(fichier,mode='w',encoding='utf8',newline='') as f:
        data = csv.DictWriter(f,clefs)
        data.writeheader()
        data.writerows(table)
        f.close()

def lire_fichier(fichier):
    table=[]
    with open(fichier,mode='r',encoding='utf8') as f:
        data=csv.DictReader(f)
        for ligne in data:
            table.append(dict(ligne))
        f.close()
    return table

        
if __name__ == '__main__':
    # 2-a) nombre de fiches de la table
    nb_fiches=len(persinfo)
    
    # 2-b) clefs des fiches de la table
    clefs=list(persinfo[0].keys())
    
    # 2-) nationalités des fiches de la table
    nationalites=[persinfo[i]['nationalité'] for i in range(len(persinfo))]
    
    # 2-d) tester la présence de Turing dans la table
    name_in_the_table=False
    k=0
    while not name_in_the_table and k < len(persinfo):
        name_in_the_table = (persinfo[k]['nom']=='ada')
        k+=1
    
    # 3-b) Recherche des noms dans la table
    personnes=chercher(persinfo,'nom')
    
    # 4-b) On teste la présence d'une fiche
    fiche1={'nom':'turing','prénom':'alan','nationalité':'anglaise','invention':'machine de turing'}
    fiche2={'nom':'lovelace','prénom':'ada','nationalité':'anglaise','invention':'calculs'}
    alan_in_the_table = est_present(persinfo,fiche1)
    ada_in_the_table = est_present(persinfo,fiche2)
    
    # 5-b) Ajouter fiche de Guido von Rossum
    ajouter_fiche(persinfo,{'nom':'von Rossum','prénom':'guido','nationalité':'néerlandaise','invention':'langage python'})
    
    # ---- Programme principal ---------------
    #------------------------------------------
    """
    table=lire_fichier('table.csv')
    saisir_fiche(table)
    ecrire_fichier('table.csv',table)
    """
                  