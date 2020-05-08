import numpy as np
import initialisation as init
import pygame
from pygame.locals import *

def moove(mat,key):
    if key == pygame.K_DOWN: #down
        moove = 1
        mat = np.rot90(mat,3)
    elif key == pygame.K_RIGHT: #right
        moove = 2
        mat = np.rot90(mat,2)
    elif key == pygame.K_UP: #up
        moove=3
        mat = np.rot90(mat,1)
    elif key == pygame.K_LEFT: 	# left on ne fait rien
        moove = 4
    return mat,moove

#fonction qui dans la version finale est inutilisee
def print_mat(mat):
    for i in range (4):
        for j in range (4):	
            print(int(mat[i][j]), end='')
            print('  ', end='')
        if j == 3:
            print("\n")
    return mat


def maj(mat,key):
    [mat,mv] = moove(mat,key)
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

def init_2048():
    return init.init_2048()




	# initialisation
	# gagner ?
	# mouvement ?
	# MATTHEO mis a jour  compresser -> Fusionner -> Compresser


	#print_mat(moove(moove(m,3),1))
