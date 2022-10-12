a=b=c=0
somme=moyenne=0
liste=[a,b,c]
for indice in range (0,3):
    while True:
        liste[indice]=int(input("Entrer un chiffre compris entre 0 et 40000"))
        if (liste[indice]>0 and liste[indice]<40000):
            somme+=(liste[indice])
            break
        print("le nombre n'est pas valide")
moyenne=somme/len(liste)
print(moyenne)