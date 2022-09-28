def affiche_menu():
    print("Menu :")
    print("Action 1")
    print("Action 2")
affiche_menu()

def dire(texte = 'bye bye'):
    print('# ' + texte) # affiche # bonjour

dire('bonjour')
dire('Au revoir')
dire()

def addition(a, b):
    return a + b 

somme = addition(8, 14) 
print(somme) # affiche 22

somme = addition(2, 3)
print(somme) # affiche 5

def saluer(prenom = 'Visiteur'):
    print('bonjour ' + prenom)

saluer('clem') # Affiche `Bonjour Clem`
saluer()

for i in range(10): #for i in range(2,10):
    print("debut iteration", i)
    print("bonjour")
    if i == 2:
        break
    print("fin iteration", i)
print("apres la boucle")

z = "orange"
y = "orange"
x = "orange"

x, y, z = "orange","orange","orange"
x=y=z="orange"
print(x, y, z)

a, b = 0, 0
print (a,b)