print("Saisir 3 nombres entiers positifs et plus petits que 40000 \n")
variable1 = int(input('Tapez la valeur de la variable1 : '))
variable2 = int(input('Tapez la valeur de la variable2 : '))
variable3 = int(input('Tapez la valeur de la variable3 : '))

print("voici les valeurs de variable1, de variable2 et variable3\n");
print("première variable = ", variable1)
print("deuxième variable = ", variable2)
print("troisième variable = ", variable3)
if variable1 < 0 or variable2 < 0 or variable3 < 0:
    print("L'une des valeurs entrées est inférieure à 0") 

if variable1 < 40000 or variable2 < 40000 or variable3 < 40000:
    total = (variable1 + variable2 + variable3)
    print("Total = ", total)

    resultat = total / 3
    print("La moyenne des valeurs entrées est: " + str(resultat))
