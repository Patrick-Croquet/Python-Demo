class color:
    BOLD = '\033[1m'

# Déclaration des variables et tableaux
Damier = [[False for j in range(8)] for i in range(8)]
Mouv = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
posi = 1
posj = 1

# Initialisation du damier
for i in range(8):
    for j in range(8):
        Damier[i][j] = False

# Saisie de la position du pion avec contrôle
Correct = False
while not Correct:
    posi = int(input("Entrez la ligne de votre pion (1 à 8) : "))
    if 1 <= posi <= 8:
        Correct = True

Correct = False
while not Correct:
    posj = int(input("Entrez la colonne de votre pion (1 à 8) : "))
    if 1 <= posj <= 8:
        Correct = True

# Positionnement du pion sur le damier virtuel
Damier[posi-1][posj-1] = True
for i in range(8):
    for j in range(8):
        print(" O " if Damier[i][j] else " X ", end="")
    print()

# Saisie du déplacement avec contrôle
print("Quel déplacement ?")
print(" - 0: en haut à gauche")
print(" - 1: en haut à droite")
print(" - 2: en bas à gauche")
print(" - 3: en bas à droite")

Correct = False
while not Correct:
    Dep = int(input("Entrez le déplacement (0 à 3) : "))
    if 0 <= Dep <= 3:
        Correct = True

# Calcul des nouvelles coordonnées du pion
i2 = posi + Mouv[Dep][0]
j2 = posj + Mouv[Dep][1]
MoveOK = (1 <= i2 <= 8) and (1 <= j2 <= 8)

# Si le déplacement est valide
if MoveOK:
    Damier[posi-1][posj-1] = False
    Damier[i2-1][j2-1] = True
    # Affichage du nouveau damier
    for i in range(8):
        for j in range(8):
            print(" O " if Damier[i][j] else " X ", end="")
        print()
else:
    print("Mouvement impossible")

print()

for i in range(1,8):
    for j in range(1,8):
        if i == j:
            Damier[i][j] = True
        print('\033[1m' '\033[95m' f" {i*j:2d} " if Damier[i][j] else '\033[0m' '\033[94m' f" {i*j:2d} ", end="")
    print('\033[0m' )

