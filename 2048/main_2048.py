import numpy as np
import initialisation as init
import perdu as lost
import mat_finale as fi

def moove(mat,way):
    if way == 2: #down
        moove = 1
        mat = np.rot90(mat,3)
    elif way ==3: #right
        moove = 2
        mat = np.rot90(mat,2)
    elif way ==5: #up
        moove=3
        mat = np.rot90(mat,1)
    elif way == 1: 	# left on ne fait rien
        moove = 4
    return mat,moove

def print_mat(mat):
    for i in range (4):
        for j in range (4):	
            print(int(mat[i][j]), end='')
            print('  ', end='')
        if j == 3:
            print("\n")
    return mat


def maj(mat,way):
    [mat,mv] = moove(mat,way)
    mat = compresser(mat)
    mat = fusion(mat)
    mat = compresser(mat)
    mat = final_mat(mat,mv)
    return mat


def fusion(mat):
	for i in range(4):
		for j in range(3):
			if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
				mat[i][j] *= 2
				mat[i][j+1] = 0
	return mat

def compresser(mat):
	
	for i in range(4):
		count_0 = 0
		for j in range(4):
			if mat[i][j] == 0:
				count_0 = count_0 + 1
			elif count_0 != 0:
				mat[i][j-count_0] = mat[i][j]
				mat[i][j] = 0
	return mat


def final_mat(mat,way):
	mat =  np.rot90(mat,way)
	return mat

if __name__ == "__main__":
    #ici on crée une nouvelle grille
    mat=init.init_2048()
    way=0
    print("Grille de depart : \n")
    print_mat(mat)
    perdu = 0
    while way != 6 or perdu ==1 :
        print("___________________________________________________________")
        print("Que voulez vous faire ? (2: down | 3: right | 5: up | 1: left | 6 : stop)")
        way = int(input())
        print("___________________________________________________________")
        if way != 6:
            #1 maj
            mat=maj(mat,way)
            #2/ On met nouvelle case
            mat = fi.grille_finale(mat)
            #3/On regarde si on a perdu
            perdu = lost.perdu(mat)
            print_mat(mat)
	

	# initialisation
	# gagner ?
	# mouvement ?
	# MATTHEO mis a jour  compresser -> Fusionner -> Compresser


	#print_mat(moove(moove(m,3),1))
