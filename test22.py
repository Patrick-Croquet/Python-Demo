# Lecture séquentielle d'un fichier texte
with open('fichier.txt', 'r') as fichier:
    for ligne in fichier:
        print(ligne.strip())  # .strip() pour supprimer les caractères de fin de ligne