def traitement_args(*args):
    for val in args:
        if type(val)==list:
            print(val[-1])
        elif type(val)==str:
            print(val.upper())


def traitement_kwargs(**kwargs):
    for key,val in kwargs.items():
        print(key+" = "+str(val))
        
def traitement_kwargs2(**kwargs):
    val1=kwargs.get('clef1',0)
    val2=kwargs.get('clef2',None)
    print(val1,val2)
        
# Unpacking explicite avec une liste, puis un dictionnaire
def aire_rectangle(a, b):
    return a*b

def aire_rectangle(cote1=0, cote2=0):
    return cote1*cote2

if __name__ == '__main__':
    rec1 = [3, 8]
    rec2 = {'cote1':4, 'cote2':8}
    # La liste rec1 va etre depaquetee en arguments unitaires
    print(aire_rectangle(*rec1))
    # Le dictionnaire rec2 va etre depaquete en arguments unitaires
    print(aire_rectangle(**rec2))
    
    traitement_args(rec1)
    traitement_kwargs(**rec2)
    traitement_kwargs2(clef1=5,clef2='vol')
    traitement_kwargs2(clef2='vol')
