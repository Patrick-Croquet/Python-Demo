def recherche_dans_tableau(tableau, element):
    # Utilisation d'un flag pour marquer la fin du tableau
    flag = -1
    position = flag
    # Parcours du tableau
    for i in range(len(tableau)):
        # Vérification si l'élément est trouvé
        if tableau[i] == element:
            position = i
            break  # Sortie de la boucle si l'élément est trouvé
    if position != flag:
        print("L'élément", element, "est trouvé à la position", position)
    else:
        print("L'élément", element, "n'est pas trouvé dans le tableau.")

# Exemple d'utilisation
tableau = [3, 5, 8, 12, 15]
element_recherche = 20
recherche_dans_tableau(tableau, element_recherche)