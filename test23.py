# Lecture et traitement des données d'un fichier texte
with open('fichier.txt', 'r') as fichier:
    lignes = fichier.readlines()  # Lecture de toutes les lignes dans une liste
    for ligne in lignes:
        # Traitement des lignes, par exemple :
        mots = ligne.split()  # Séparation de la ligne en mots
        print("Nombre de mots dans la ligne :", len(mots))
        print(mots[3])

