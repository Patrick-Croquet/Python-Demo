# Tri des lignes d'un fichier texte
with open('fichier.txt', 'r') as fichier:
    lignes = fichier.readlines()
    lignes_triees = sorted(lignes)  # Tri des lignes
    for ligne in lignes_triees:
        print(ligne.strip())
