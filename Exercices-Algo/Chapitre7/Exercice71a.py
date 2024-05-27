# Saisie du nombre de valeurs
Nb = int(input("Entrez le nombre de valeurs : "))

# Redimensionnement du tableau T
T = [0] * Nb

# Saisie des valeurs dans le tableau
for i in range(Nb):
    T[i] = int(input("Entrez le nombre n° " + str(i + 1) + " : "))

# Initialisation du drapeau (flag) à True
Flag = True

# Vérification si les nombres sont consécutifs
for i in range(1, Nb):
    if T[i] != T[i - 1] + 1:
        Flag = False
        break

# Affichage du résultat
if Flag:
    print("Les nombres sont consécutifs")
else:
    print("Les nombres ne sont pas consécutifs")