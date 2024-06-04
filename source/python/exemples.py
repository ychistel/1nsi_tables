from csv import DictReader,DictWriter

trajets=[]
reservations=[]

with open('trajets.csv', mode='r', encoding='utf8') as f:
    data=DictReader(f,delimiter=',')
    for ligne in data:
        trajets.append(dict(ligne))
    f.close()

with open('reserve.csv', mode='r', encoding='utf8') as f:
    data=DictReader(f,delimiter=',')
    for ligne in data:
        reservations.append(dict(ligne))
    f.close()
    
# 1) réservation d'olivia marie :
def quelle_reservation(nom,prenom):
    for dico in reservations:
        if dico['nom']==nom and dico['prénom']==prenom:
            return dico['trajet']
            
            
if __name__ == '__main__':
    trjt=quelle_reservation('marie','olivia')