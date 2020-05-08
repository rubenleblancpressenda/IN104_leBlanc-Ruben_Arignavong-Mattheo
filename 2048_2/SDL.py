#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:48:40 2020

@author: mattheo
"""
import numpy as np
import perdu as lost
import mat_finale as fi
import main_2048_sdl as main
import getCouleur
import copy 
import SDL
import pygame
from pygame.locals import *

TAILLE = 4
BLACK = (25, 158, 156)

def init_mat():
    return main.init_2048()

def affiche_mat(fenetre,mat):
    global TAILLE
    
    fenetre.fill(BLACK)#avant de dessiner on remplit de noire la fenetre

    for i in range(TAILLE):
        for j in range(TAILLE):
            pygame.draw.rect(fenetre, getCouleur.getCouleur(mat[i][j]), (j*(400/TAILLE), i*(400/TAILLE), 400/TAILLE, 400/TAILLE))
            label = police.render(str(mat[i][j]), 1, (5,25,55))
            fenetre.blit(label, (j*(400/TAILLE)+30, i*(400/TAILLE)+30))
    pass



def afficher_perdu():
    pass


def checkFleche(key):
	return(key == pygame.K_UP or key == pygame.K_DOWN or key == pygame.K_LEFT or key == pygame.K_RIGHT)


if __name__ == "__main__":
    #mat = [[2,0,2,0][4,2,4,0][8,16,2,0][8,32,16,64]]
    #On initialise la fenetre
    mat = pygame.init()
    fenetre = pygame.display.set_mode((400, 400),0,32)
    pygame.display.set_caption("2048")
    pygame.draw.rect(fenetre, (4), (20,20, 100, 100))
    
    police = pygame.font.SysFont("monospace", 25)   #On initialise la première grille et on l'affiche
    mat = init_mat()
    
    #On affiche la matrice initiale
    main.print_mat(mat)
    affiche_mat(fenetre,mat)
    pygame.display.update()
    play = True
    while play == True:
        for event in pygame.event.get():   #On parcours la liste de tous les evenements reçus
            pygame.display.update()
            #Conditions pour quitter le jeu
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) : 
                pygame.quit()      #Si un de ces evenements est de type QUIT
                play = False      #On arrete la boucle
            #Conditions pour jouer  (fleche)
            if lost.perdu(mat) == False:
                if event.type == KEYDOWN:
                    if checkFleche(event.key):
                        key = event.key
                        old = copy.deepcopy(mat)#on est ici obligé de travailler avec copy
                        #on travail avec un tableau donc les sauvegarde ne peut se faire que comme cela ou avec un code maison
                        mat = main.maj(mat,key)
                        #Si après maj la nouvelle grille égale à l'ancienne on ne fait rien
                        if not np.array_equal(old,mat):
                        #2/ On met nouvelle case
                            mat = fi.grille_finale(mat)
            else:
                afficher_perdu()
                print("hey")
                main.print_mat(mat)
            affiche_mat(fenetre,mat)
                        
                