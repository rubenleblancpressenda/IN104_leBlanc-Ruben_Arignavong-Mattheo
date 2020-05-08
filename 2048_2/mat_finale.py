
import numpy as np
from random import *
    

def grille_finale(grille):
    A=[]
    for i in range(4):
        for j in range(4):
            if grille[i][j]==0:
                A.append([i,j])
            j=j+1
        i=i+1

    alea = randint(0, len(A)-1)
    case=A[alea]
    valeur = np.random.choice([2,2,2,2,2,2,2,2,2,4],1)
    grille[case[0]][case[1]]=valeur
    return(grille)
    

