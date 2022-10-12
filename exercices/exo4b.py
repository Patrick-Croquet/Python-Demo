n=float(input("saisir un nombre"))
bas=0.0
haut=n
moyenne=(haut+bas)/2

while ((haut-bas)>0.001):
    if (moyenne*moyenne>n):
        haut=moyenne
    elif (moyenne*moyenne<n):
        bas=moyenne
    moyenne=(haut+bas)/2
    print(str(bas) + " et " + str(haut))
print(moyenne*moyenne)
