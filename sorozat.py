
import random

lista=[]

def szerencse():
    for i in range(0,7,1):
        lista.append(random.randint(0,1))
        if i <7:
            print(lista,end="-")
        else:
            print(lista,end="")    
                    

def fejek_szama(lista):
    return lista.count(1)

