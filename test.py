a=7
print(a + 3)
b=2
print(a + b)
c = a//b
d = a%b
print(str(c) +' et '+ str(d))
a, b = 4, 5.2
print(str(a) +' et '+ str(b)) 
a, b = b, a
print(str(a) +' et '+ str(b)) 
print(type(1)) # Affiche <class 'int'>
print(type(1.0)) # Affiche <class 'float'>
chaine = 'Et voilà du texte'
print(chaine)
chaine = 'Nous l\'avons'
chaine2 = "\"réparé\""
print(chaine + " " + chaine2)
reponse = input() # Une ligne vide apparait et attend que l'utilisateur entre une information

age = input("Age : ") # "Age : " est affiché en début de ligne puis attend une information
# `age` et `reponse` contiennent ce que l'utilisateur a entré
print(age)

age = int(input("Quel est votre âge ? ")) # Souvenez-vous, il faut convertir en un entier

if age > 16: # Si l'âge est strictement supérieur à 16 (ans)
    print("Vous avez plus de 16 ans :)")
elif age < 0: # Si l'âge est strictement inférieur à 0
    print("Tu te moquerais pas de moi ?")
else: # Dans tous les autres cas
    print("Tu es encore un peu jeune")
print("Au revoir")

vrai = True # Notez bien la majuscule
faux = False # Ici aussi
print(type(vrai)) # Affiche <class 'bool'>

print(7 > 5 > 1) # Affiche True
print(7 > 5 < 9 != 10) # Affiche True