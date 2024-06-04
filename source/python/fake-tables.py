from faker import Faker
import random,csv

fake=Faker('fr_FR')
villes=['caen','rouen','alençon','le mans','lille',\
       'brest','rennes','vannes','cherbourg','paris',\
       'évreux','strasbourg','lyon','marseille',\
       'nantes','bordeaux','la rochelle','mulhouse',\
        'amiens','toulouse','montpelier','toulon',\
        'grenoble','orléans','tours','angers']
inscrits=[{'id_inscrit':0,'nom':'','prénom':'','âge':0,'tel':''}]
trajets=[{'id_trajet':0,'départ':'','arrivée':'','date':'','inscrit':0,'nb_place':0,'nb_reserv':0}]
reservations=[{'id_reserv':0,'trajet':0,'inscrit':0}]
N=250


# Création de la table inscrits
#-------------------------------
for k in range(1,100):
    dico=dict()
    dico['id_inscrit']=k
    dico['nom']=fake.last_name()
    dico['prénom']=fake.first_name()
    dico['âge']=random.randint(20,60)
    dico['tel']=fake.phone_number()
    inscrits.append(dico)

# Création de la table trajets
#-------------------------------
for k in range(1,150):
    dico=dict()
    dico['id_trajet']=k
    dico['départ']=random.choice(villes)
    i=villes.index(dico['départ'])
    dico['arrivée']=random.choice(villes[0:i]+villes[i+1:len(villes)])
    dico['inscrit']=random.choice(inscrits)['id_inscrit']
    dico['date']=fake.future_date(end_date='+15d')
    dico['nb_place']=random.randint(1,4)
    dico['nb_reserv']=0
    trajets.append(dico)

# Création de la table reservations
#-----------------------------------
for k in range(1,80):
    dico=dict()
    dico['id_reserv']=k
    dico['inscrit']=random.choice(inscrits)['id_inscrit']
    dico['trajet']=random.choice(trajets)['id_trajet']
    if trajets[dico['trajet']]['nb_reserv'] < trajets[dico['trajet']]['nb_place']:
        trajets[dico['trajet']]['nb_reserv']+=1
        reservations.append(dico)


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

def creer_test(op='and',**kwargs):
    test=''
    i=0
    for clef,valeur in kwargs.items():
        test+='dico["'+clef+'"]=="'+str(valeur)+'"'
        i+=1
        if i<len(kwargs):
            test+=' '+op+' '
    return test


def chercher(table,**kwargs):
    # on initialise la table résultat qui contient les dicos trajets répondant à la recherche
    resultat=[]
    for clef in kwargs.keys():
        if clef in table[0].keys():
            # on crée un test avec les différents paramètre de recherche
            test=creer_test('and',**kwargs)
            #print(test)
            for dico in table:
                if eval(test):
                    resultat.append(dico)
    return resultat

def ajouter(table,**kwargs):
    print(kwargs)
    for dico in table:
        print(dico)
        if kwargs != dico:
            print('ok, pas dans la table')
        else:
            print(dico,'dans la table')
            break
            
    
def reserver_trajet(id_trajet,id_inscrit):
    dico=trajets[id_trajet]
    if dico['nb_reserv'] < dico['nb_place']:
        print('ok, on réserve')
    else:
        print('complet')
    
    

def afficher(table):
    for dico in table:
        print(dico)

if __name__ == '__main__' :

    ecrire_fichier('trajet2.csv',trajets)
    ecrire_fichier('inscrit2.csv',inscrits)
    ecrire_fichier('reserve2.csv',reservations)

    trajet=lire_fichier('trajet2.csv')
    inscrit=lire_fichier('inscrit2.csv')
    reservation=lire_fichier('reserve2.csv')

    # Requêtes sur tables
    reponse=[]
    for dico in inscrit:
        if dico['id_inscrit']=='77':
            reponse.append(dico)
    print(reponse)
    
    reponse=[]
    for dico in trajet:
        if dico['départ']=='caen':
            reponse.append(dico)
    print(reponse)

    reponse=[]
    for dico in trajet:
        if dico['date']=='2021-06-06':
            reponse.append(dico)
    print(reponse)

    reponse=[]
    for dico in trajet:
        if dico['départ']=='marseille' and dico['arrivée']=='nantes':
            reponse.append(dico)
    print(reponse)

    
    reponse=[]
    for dico in trajet:
        if dico['départ']=='marseille' or dico['arrivée']=='nantes':
            reponse.append(dico)
    print(reponse)
    
    
    reponse=[]
    for dico in inscrit:
        if 20 <= eval(dico['âge']) <= 40:
            reponse.append(dico)
    print(reponse)
    
    reponse=[]
    for dico in inscrit:
        if dico['prénom'] == 'Alice':
            reponse.append((dico['id_inscrit'],dico['tel']))
    print(reponse)
    
    reponse=[]
    for dico1 in trajet:
        if dico1['départ']=='caen':
            for dico2 in inscrit:
                if dico2['id_inscrit']==dico1['inscrit']:
                    rep={
                        'départ':dico1['départ'],
                        'arrivée':dico1['arrivée'],
                        'date':dico1['date'],
                        'nom':dico2['nom'],
                        'prénom':dico2['prénom']
                        }
                    reponse.append(rep)
    print(reponse)
    
    reponse=[]
    for dico1 in inscrit:
        if dico1['prénom'] == 'Alex' and dico1['nom'] == 'Techer':
            for dico2 in trajet:
                if dico2['inscrit']==dico1['id_inscrit']:
                    rep={
                        'départ':dico2['départ'],
                        'arrivée':dico2['arrivée'],
                        'date':dico2['date']
                        }
                    reponse.append(rep)
    print(reponse)    
    #afficher(trajets)
    
    reponse=[]
    for dico in reservation:
        if dico['id_reserv'] == '25':
            for dico1 in trajet:
                if dico1['id_trajet']==dico['trajet']:
                    rep=dico1
            for dico2 in inscrit:
                if dico2['id_inscrit']==dico['inscrit']:
                    rep.update(dico2)
            reponse.append(rep)
    print(reponse)        

    # C) 3-b
    reponse=[]
    
    for dico in reservation:
        rep={}
        for dico1 in trajet:
            if dico1['id_trajet'] == dico['trajet'] and dico1['date']=='2021-06-06':
                for dico2 in inscrit:
                    if dico2['id_inscrit']==dico['inscrit']:
                        rep['reserve']=dico['id_reserv']
                        rep['date']=dico1['date']
                        rep['départ']=dico1['départ']
                        rep['arrivée']=dico1['arrivée']
                        rep['nom']=dico2['nom']
                        rep['prénom']=dico2['prénom']
                        reponse.append(rep)
                    else:
                        continue
            else:
                continue
    print(reponse)
    """
    # C) 4-a-b-c
    # on récupère le dernier id_inscrit de la table
    nouvel_inscrit={
        'id_inscrit' : str(eval(inscrit[-1]['id_inscrit'])+1),
        'nom' : 'Belin',
        'prénom' : 'Pierre',
        'âge' : '29',
        'tel' : '0231445566'
        }
    inscrit.append(nouvel_inscrit)
    
    nouveau_trajet={
        'id_trajet' : str(eval(trajet[-1]['id_trajet'])+1),
        'départ' : 'caen',
        'arrivée' : 'paris',
        'date' : '2021-06-05',
        'nb_place' : '3',
        'nb_reserv' : '0'
        }
    for dico in inscrit:
        if dico['nom'] == 'Belin' and dico['prénom']=='Pierre':
            nouveau_trajet['inscrit']=dico['id_inscrit']
    print(nouveau_trajet)
    
    nouvelle_reservation={}
    for dico in trajet:
        if dico['départ'] == 'paris' and dico['arrivée']=='amiens' and dico['date'] == '2021-06-02' and eval(dico['nb_reserv']) < eval(dico['nb_place']):
            nouvelle_reservation={
                'id_reserv' : str(eval(reservation[-1]['id_reserv'])+1)
            }
            nouvelle_reservation['trajet']=dico['id_trajet']
            dico['nb_reserv']=str(eval(dico['nb_reserv'])+1)
            for dico in inscrit:
                if dico['nom'] == 'Belin' and dico['prénom']=='Pierre':
                    nouvelle_reservation['inscrit']=dico['id_inscrit']
    print(nouvelle_reservation)
    """
    """
    reponse=chercher(trajet,départ='caen')
    afficher(reponse)
    """
