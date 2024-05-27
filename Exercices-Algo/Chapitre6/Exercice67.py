# Déclaration du tableau de notes
Notes = [0] * 9
somme = 0
# Boucle pour lire les notes
for i in range(9):
    print("Entrez la note numéro", i + 1)
    Notes[i] = float(input())
    somme += Notes[i]

# Affichage des notes
print("Les notes saisies sont :", Notes)

# Affichage de la moyenne
print("La moyenne des notes est :", somme/9)