a = 5
print(a) 
b = 8.2
print(a + b)

a = b + 1
print(a)

c = 1
"""c = c + 3"""
c += 3
print(c)

a, b = 4, 5.2
print(a,b)
print(type(a))
print(type(b))
"""c = a
a = b
b = c"""

a, b = b, a

print(a,b)
print(type(a))
print(type(b))
chaine = "Et voilà, du texte aujourd'hui"
print(chaine)

var  = 10
print(var)
print(type(var))
var = str(var)
print(type(var))
var = float(var)
print(type(var))
print(var)
var = int(var)
print(var)

# reponse = input() # Une ligne vide apparait et attend que l'utilisateur entre une information
# age = input("Age : ") # "Age : " est affiché en début de ligne puis attend une information
# `age` et `reponse` contiennent ce que l'utilisateur a entré

#print(age, reponse)

age = int(input("Quel est votre âge ? "))

if age > 18:
    print("Vous êtes majeur")
