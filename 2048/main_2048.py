import numpy as np

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
			print(mat[i][j], end='')
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
    m=[[0,2,0,4],[4,4,0,4],[4,0,0,2],[0,0,2,2]]
    way=0
    print("Grille de depart : \n")
    print_mat(m)
    while way != 6 :
        print("___________________________________________________________")
        print("Que voulez vous faire ? (2: down | 3: right | 4: up | 1: left | 6 : stop)")
        way = int(input())
        if way != 5:
            m=maj(m,way)
            print_mat(m)
	

	# initialisation
	# gagner ?
	# mouvement ?
	# MATTHEO mis a jour  compresser -> Fusionner -> Compresser


	#print_mat(moove(moove(m,3),1))
