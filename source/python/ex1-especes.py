import csv

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
    if fiche!={} and not est_present(table,fiche):
        table.append(fiche)
    
def saisir_fiche(table,attributs):
    while True:
        rep=input("Saisir une nouvelle fiche ? (o/n)")
        if rep=='o' or rep=='O':
            fiche=dict()
            for clef in attributs:
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
    attributs=[]
    with open(fichier,mode='r',encoding='utf8') as f:
        data=csv.DictReader(f)
        for ligne in data:
            table.append(dict(ligne))
        f.close()
    return table

def lire_attributs_fichier(fichier):
    with open(fichier,mode='r',encoding='utf8') as f:
        data=csv.reader(f,delimiter=',')
        for ligne in data:
            attributs=ligne
        f.close()
    return attributs

if __name__ == '__main__':
    table=lire_fichier('espece.csv')
    
    

                  