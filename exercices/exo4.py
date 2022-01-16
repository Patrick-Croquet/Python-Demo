n = int(input('Entrez un nombre entier : '))

intervalle = .001
NBas = 0
NHaut = n
i = 0

while NHaut - NBas > intervalle:
    Valeur = (NHaut + NBas)/2
    print("On teste la valeur ", Valeur)
    Nombre = Valeur * Valeur
    if Nombre > n :
      print (Valeur, "x", Valeur, "=", Nombre,". Le résultat est",  Nombre, "supérieur à", n)
      NHaut = Valeur
    else :
      print (Valeur, "x", Valeur, "=", Nombre,". Le résultat est",  Nombre, "inférieur à", n)
      NBas = Valeur       
      
    print ("Donc le nombre recherché est donc compris entre", NBas, "et", NHaut)
