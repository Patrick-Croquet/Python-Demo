tableau2 = [5, 2, 9, 1, 7]
tableau3 = [4, 6, 10, 3, 8]

# Exemple d'utilisation :
tableau = tableau2 + tableau3
n = len(tableau)

# Parcourir chaque élément du tableau
for i in range(n-1):

    max_index = i
    for j in range(i + 1, n):
        if tableau[j] < tableau[max_index]:
            max_index = j
    # Échanger l'élément maximum avec l'élément à la position actuelle        
    tableau[i], tableau[max_index] = tableau[max_index], tableau[i]

print("Tableau trié par sélection croissante :", tableau)