def TriTableau(T, n, Croissant):
    for i in range(0, n - 1):
        pos = i
        for j in range(i + 1, n):
            if Croissant:
                if T[j] < T[pos]:
                    pos = j
            else:
                if T[j] > T[pos]:
                    pos = j
        temp = T[pos]
        T[pos] = T[i]
        T[i] = temp

Tableau = [5,7,2,6,3]
TriTableau(Tableau, len(Tableau), False)
print(Tableau)