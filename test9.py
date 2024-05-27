def tri_selection(tableau):
    n = len(tableau)
    # Parcourir chaque élément du tableau
    for i in range(n):
        # Trouver l'indice du minimum restant dans le tableau non trié
        min_index = i
        for j in range(i+1, n):
            if tableau[j] < tableau[min_index]:
                min_index = j
        # Échanger l'élément minimum avec l'élément à la position actuelle
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]

# Exemple d'utilisation
tableau = [64, 25, 12, 22, 11]
tri_selection(tableau)
print("Tableau trié par sélection:")
for i in range(len(tableau)):
    print("%d" %tableau[i]),