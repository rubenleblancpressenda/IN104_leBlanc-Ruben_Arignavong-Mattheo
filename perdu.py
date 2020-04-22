def perdu(grille):
    n=0
    for i in range(3):
        for j in range(3):
            if grille[i][j]==grille[i+1][j] or grille[i][j]==grille[i][j+1]:
                n=1
            j=j+1
            if grille[i][3]==grille[i+1][3] or grille[3][i]==grille[3][i+1]:
                n=1
        i=i+1
    if n==0:
        print("vous avez perdu")
    
