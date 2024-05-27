# Demande à l'utilisateur d'entrer le nombre de notes à saisir
Nb = int(input("Entrez le nombre de notes à saisir : "))

# Redimensionnement du tableau T
T = [0] * Nb

# Lecture des notes
for i in range(Nb):
    T[i] = float(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Calcul de la somme des notes
Somme = 0
for i in range(Nb):
    Somme += T[i]

# Calcul de la moyenne
Moyenne = Somme / Nb

# Comptage du nombre d'élèves dépassant la moyenne
NbSup = 0
for i in range(Nb):
    if T[i] > Moyenne:
        NbSup += 1

# Affichage du nombre d'élèves dépassant la moyenne
print(NbSup, "élèves dépassent la moyenne de la classe")