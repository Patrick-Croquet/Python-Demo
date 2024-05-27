# Supposons que les tableaux T1 et T2 sont déjà saisis
T1 = [4, 8, 7, 9, 1, 5, 4, 6, 7]  # Exemple de tableau T1 saisi
T2 = [7, 6, 5, 2, 1, 3, 7, 4]  # Exemple de tableau T2 saisi

# Détermination de la taille des tableaux T1 et T2
N = min(len(T1), len(T2))

# Création du tableau T3 de même taille que T1 et T2
T3 = [0] * N

# Calcul de la somme des éléments des tableaux T1 et T2
for i in range(N):
    T3[i] = T1[i] + T2[i]

# Affichage du tableau T3
print("Tableau T3 après addition de T1 et T2 :", T3)
