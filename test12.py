def recherche_dichotomique(tableau, element):
    debut = 0
    fin = len(tableau) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        # Si l'élément est présent au milieu
        if tableau[milieu] == element:
            return milieu
        # Si l'élément est plus petit, rechercher dans la première moitié
        elif tableau[milieu] < element:
            debut = milieu + 1
        # Sinon, rechercher dans la deuxième moitié
        else:
            fin = milieu - 1
    # Si l'élément n'est pas présent dans le tableau
    return -1

# Exemple d'utilisation
tableau = [2, 3, 4, 10, 40]
element_recherche = 4
resultat = recherche_dichotomique(tableau, element_recherche)
if resultat != -1:
    print("L'élément", element_recherche, "est trouvé à la position", resultat)
else:
    print("L'élément", element_recherche, "n'est pas trouvé dans le tableau.")