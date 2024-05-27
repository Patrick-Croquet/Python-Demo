# Déclaration des variables i, Somme
Somme = 0

# Supposons que le tableau T est déjà saisi
Tableau = [1, 2, 3, 4, 5]  # Exemple de tableau saisi

# Calcul de la somme des éléments du tableau
for i in range(len(Tableau)):
    Somme += Tableau[i]

# Affichage de la somme
print("Somme des éléments du tableau :", Somme)