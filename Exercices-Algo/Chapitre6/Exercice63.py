# Déclaration du tableau de notes
Notes = [0] * 9

# Boucle pour lire les notes
for i in range(9):
    print("Entrez la note numéro", i + 1)
    Notes[i] = int(input())

# Affichage des notes
print("Les notes saisies sont :", Notes)