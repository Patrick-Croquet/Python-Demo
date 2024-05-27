# Création et écriture dans un fichier texte de manière séquentielle
with open('fichier.txt', 'w') as fichier:
    fichier.write("Premiere ligne : 1\n")
    fichier.write("Deuxieme ligne : 2\n")
    fichier.write("Troisieme ligne : 3\n")
    fichier.write("Quatrieme ligne : 4\n")