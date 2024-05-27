def TableauCroissant(T, n):
    Flag = True
    i = 0
    while Flag and i < n - 1:
        Flag = T[i] < T[i + 1]
        i += 1
    return Flag

# Tableau = [5,3,2,6,4]
Tableau = [2,3,4,5,6]
print(TableauCroissant(Tableau, len(Tableau)))