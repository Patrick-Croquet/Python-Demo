def tri_bulles_decroissant(tab):
    n = len(tab)
    for i in range(n):
        flag = False  # Initialisation du drapeau
        for j in range(0, n - i - 1):
            if tab[j] < tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
                flag = True  # Marquer que des échanges ont été effectués
        if not flag:
            break  # Si aucun échange n'a été effectué, le tableau est déjà trié

# Exemple d'utilisation :
tableau = [5, 2, 9, 1, 7]
tri_bulles_decroissant(tableau)
print("Tableau trié à bulles décroissante :", tableau)