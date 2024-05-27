# Exemple d'algorithme fonctionnel avec map()
def carre(x):
    return x ** 2

liste = [1, 2, 3, 4, 5]

resultat = list(map(carre, liste))
print("Résultat de l'application de la fonction carré à chaque élément de la liste :", resultat)
