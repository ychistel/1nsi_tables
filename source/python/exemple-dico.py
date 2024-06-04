capitale={
    'france':'paris',\
    'italie':'rome',\
    'allemagne':'berlin',\
    'brésil':'brasilia'
    }
continent={
    'france':'europe',\
    'italie':'europe',\
    'allemagne':'europe',\
    'brésil':'amérique'
    }
population={
    'france':67,\
    'italie':61,\
    'allemagne':83,\
    'brésil':211
    }

littoral={}

def infos(pays):
    liste=[]
    liste.append(capitale[pays])
    liste.append(continent[pays])
    liste.append(population[pays])
    return liste

suisse={'nom':'suisse','capitale':'berne','continent':'europe','population':8}
argentine={'nom':'argentine','capitale':'buenos aires','population':45,'continent':'amérique'}

def ajouter(pays):
    capitale[pays['nom']]=pays['capitale']
    continent[pays['nom']]=pays['continent']
    population[pays['nom']]=pays['population']

def ajout_littoral():
    while True:
        pays = input("pays: ")
        lit = input("littoral ? v/f : ")
        if lit == "v":
            littoral[pays]=True
        elif lit== "f":
            littoral[pays]=False
        else:
            break
        
ajouter(argentine)
ajout_littoral()
