
#la strategie de base est de priviligier seulement deux directions pour conserver les grandes cases dans un coin.
#mais, comment choisir entre ses deux directions ?

#la premiere strategie est de fusionner en priorite les deux cases identiques de plus grande valeur
def strat1(mat):
    sens=0 #sens=5 si on va vers le haut et sens=4 si on va a gauche
    h=2
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]>h :
                sens=4
                h=mat[i][j]
            elif mat[j][i]==mat[j+1][i] and mat[j][i]>h :
                sens=5
                h=mat[j][i]
    return sens



#la seconde strat consiste a choisir la direction ou l'on fusionne le plus de cases
def strat2(mat):
    sens=0
    lign=0
    col=0
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1]:
                lign=lign+1
            elif mat[j][i]==mat[j+1][i]:
                col=col+1
    if col=>lign and col!=0 :
        sens=5
    if lign>col :
        sens=4
    return sens


def tour(mat,strat):
    if strat=1 :
        sens = strat1(mat)
    if strat=2 :
        sens=strat2(mat)
    if sens != 0:  # il y a au moins deux cases identiques a cote
        mat = maj(mat, sens)

    else:  # la strat ne permet pas de choisir la direction on choisit par defaut le haut
        gauche=0
        haut=0
        for i in range(4):
            if mat[1][i]==0:
                haut=haut+1
            elif mat[i][1]==0
                gauche=gauche+1
        if mat != maj(mat, 5) :  # on peut jouer la direction haut
            mat = maj(mat, 5)
        elif mat != maj(mat, 4):
            mat = maj(mat, 4)
        elif mat != maj(mat, 2) and gauche<=haut:  # cas critique : on ne peut pas respecter la strategie de base donc on va dans la
            #la direction qui perturbe le moins la grille : on va ici vers le bas car il y a plus de cases vides
            #sur la ligne du haut que sur la colonne de gauche
            mat = maj(mat, 2)
        else:
            mat = maj(mat, 3)
    mat = fi.grille_finale(mat)
    print_mat(mat)