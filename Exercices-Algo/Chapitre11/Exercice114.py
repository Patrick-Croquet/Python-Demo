def PurgeSimple(a, b):
    Sortie = ''
    for i in range(0, len(a)):
        if a[i] != b:
            Sortie += a[i]
    return Sortie

resultat1 = PurgeSimple("Bonjour","o")
resultat2 = PurgeSimple("J'ai horreur des espaces"," ")
resultat3 = PurgeSimple("Moi, je m'en fous", "y")
print(resultat1, resultat2, resultat3)