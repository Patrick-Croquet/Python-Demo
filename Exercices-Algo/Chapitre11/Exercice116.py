def TriTableau(T, n):
    for i in range(0, n - 1):
        posmini = i
        for j in range(i + 1, n):
            if T[j] < T[posmini]:
                posmini = j
        #temp = T[posmini]
        #T[posmini] = T[i]
        #T[i] = temp
        T[posmini], T[i] = T[i], T[posmini]

Tableau = [5,7,2,6,3]
TriTableau(Tableau, len(Tableau))
print(Tableau)