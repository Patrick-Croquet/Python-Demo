def tri_bulle(tableau):
    n = len(tableau)
    # Parcourir le tableau
    for i in range(n):
        # Drapeau pour indiquer si un échange a été effectué dans cette itération
        echange_effectue = False
        # Parcourir le tableau jusqu'à l'avant-dernier élément
        for j in range(0, n-i-1):
            # Comparer les éléments adjacents et les échanger s'ils sont dans le mauvais ordre
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
                echange_effectue = True
        # Si aucun échange n'a été effectué dans cette itération, le tableau est trié
        if not echange_effectue:
            break

# Exemple d'utilisation
tableau = [64, 34, 25, 12, 22, 11, 90]
tri_bulle(tableau)
print("Tableau trié par le tri à bulle:")
for i in range(len(tableau)):
    print("%d" % tableau[i]),