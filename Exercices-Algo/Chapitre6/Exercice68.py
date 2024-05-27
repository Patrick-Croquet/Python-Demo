# Déclaration des variables Nb, Nbpos, Nbneg
Nb = 0
Nbpos = 0
Nbneg = 0

# Demande à l'utilisateur le nombre de valeurs
print("Entrez le nombre de valeurs :")
Nb = int(input())

# Redimensionnement du tableau T
T = [0] * Nb

# Boucle pour lire les valeurs et compter les valeurs positives et négatives
for i in range(Nb):
    print("Entrez le nombre n°", i + 1)
    T[i] = float(input())
    if T[i] > 0:
        Nbpos += 1
    else:
        Nbneg += 1

# Affichage du nombre de valeurs positives et négatives
print("Nombre de valeurs positives :", Nbpos)
print("Nombre de valeurs négatives :", Nbneg)
