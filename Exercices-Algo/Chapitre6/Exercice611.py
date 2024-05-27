# Supposons que les tableaux T1 et T2 sont déjà saisis
T1 = [4, 8, 7, 12]  # Exemple de tableau T1 saisi
T2 = [3, 6]  # Exemple de tableau T2 saisi

# Détermination des tailles des tableaux T1 et T2
N1 = len(T1)
N2 = len(T2)

# Initialisation de la variable S
Somme = 0

# Calcul du produit scalaire des tableaux T1 et T2
for i in range(N1):
    for j in range(N2):
        Somme += T1[i] * T2[j]

# Affichage du résultat
print("Le schtroumpf est :", Somme)