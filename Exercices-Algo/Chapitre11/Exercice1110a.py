import random

Sudok = [[0 for j in range(3)] for i in range(3)]


def RemplitGrille(T):
    for i in range(3):
        for j in range(3):
            T[i][j] = random.randint(1, 9)

def TousDifférents(T):
    for i in range(0, 8):
        for j in range(i + 1, 9):
            if T[i] == T[j]:
                return False
    return True

def VerifLignes(Grille):
    Ligne = [0] * 9
    for i in range(9):
        for j in range(9):
            Ligne[j] = Grille[i][j]
        if not TousDifférents(Ligne):
            return False
    return True

def VerifColonnes(Grille):
    Colonne = [0] * 9
    for j in range(9):
        for i in range(9):
            Colonne[i] = Grille[i][j]
        if not TousDifférents(Colonne):
            return False
    return True

def VerifSousGrilles(Grille):
    SousGrille = [0] * 3
    for ancrei in range(0, 7, 3):
        for ancrej in range(0, 7, 3):
            for decali in range(3):
                for decalj in range(3):
                    SousGrille[decali * 3 + decalj] = Grille[ancrei + decali][ancrej + decalj]
            if not TousDifférents(SousGrille):
                return False
    return True

def principale():
    RemplitGrille(Sudok)
    # while not VerifLignes(Sudok) or not VerifColonnes(Sudok) or not VerifSousGrilles(Sudok):
        # RemplitGrille(Sudok)

# principale()

chiffre = 1
for i in range(3):
    for j in range(3):
        Sudok[i][j] = chiffre
        chiffre += 1

# Affichage des valeurs du tableau
for i in range(3):
    for j in range(3):
        print('\033[1m' '\033[95m' f" {Sudok[i][j]} " if Sudok[i][j] else '\033[0m' '\033[94m' f" {Sudok[i][j]} ", end="")
    print('\033[0m' )


