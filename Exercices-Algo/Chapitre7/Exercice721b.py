def tri_selection_decroissant(tab):
    n = len(tab)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if tab[j] > tab[max_index]:
                max_index = j
        # Échanger l'élément maximum avec l'élément à la position actuelle        
        tab[i], tab[max_index] = tab[max_index], tab[i]

# Exemple d'utilisation :
tableau = [5, 2, 9, 1, 7]
tri_selection_decroissant(tableau)
print("Tableau trié par sélection décroissante :", tableau)