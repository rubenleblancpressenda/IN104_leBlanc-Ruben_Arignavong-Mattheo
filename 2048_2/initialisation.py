
import numpy as np


def init_2048():
    grille=np.zeros((4,4))
    A=np.random.choice([2,2,2,2,2,2,2,2,2,4],2) #on tire les deux chiffres initiaux selon leurs probabilités
    case1=np.random.choice([0,1,2,3],2)
    case2=np.random.choice([0,1,2,3],2)

    while case1[0]==case2[0] and case1[1]==case2[1]:
        case2=np.random.choice([0,1,2,3],2)#on choisit deux cases différentes
    grille[case1[0]][case1[1]]=A[0]
    grille[case2[0]][case2[1]]=A[1]
    return grille






