def NbVoyelles(Mot):
    compteur = 0
    for i in range(0, len(Mot)):
        if Mot[i] in "aeiouy":
            compteur += 1
    return compteur

print(NbVoyelles("Patou")) # résultat 3