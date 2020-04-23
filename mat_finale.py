def grille_finale(grille):
    A=[]
    for i in range(4):
        for j in range(4):
            if grille[i][j]==0:
                A.append([i,j])
            j=j+1
        i=i+1
    case=numpy.random.choice(A)
    valeur=random.choice(numpy.array([2,2,2,2,2,2,2,2,2,4],1))
    grille[case[0]][case[1]]=valeur
    return(grille)
    
