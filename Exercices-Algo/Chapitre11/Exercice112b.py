def NbVoyelles(Mot, voyelles):
    compteur = 0
    for i in range(0, len(Mot)):
        if Mot[i] in voyelles:
            compteur += 1
    return compteur

print(NbVoyelles("Patou", "aeiouy")) # résultat 3