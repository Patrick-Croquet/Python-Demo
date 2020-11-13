""" Exercice 1 """
age = int(input("Quel est votre age ? : "))
if age < 18:
    print ("Désolé, vous êtes mineur...")
else:
    print ("Vous êtes majeur !")

""" Exercice 2 """
nombre = int(input("Quelle table de multiplication souhaitez vous voir : "))
print("\n Avec la boucle while : \n")
print("Voici la table de multiplication de", nombre)
i = 0
while i<=10:
    print(i, " x ", nombre, " = ", nombre * i)
    i += 1


# nombre = int(input("La table de multiplication que vous souhaitez voir : "))
print("\n Avec la boucle for : \n")
print("Voici la table de multiplication de", nombre)
for x in range(1,11):
    print(x, " x ", nombre, " = ",x*nombre)

  