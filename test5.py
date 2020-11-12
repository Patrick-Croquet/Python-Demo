a = 42
def affichage():
    print(a)
affichage() # Affiche 42

a = 42
def change(valeur):
    global a   # variable globale
    a = valeur

print(a) # Affiche `42`
change(10)
print(a) # Affiche ... `10` 

# fonction anonyme
fonction = lambda a, b: a**b
print(fonction(2,3)) # Affiche 8

def test(f, a, b=None):
    if b != None:
        r = f(a, b)
    else:
        r = f(a)
    if r:
        print("Test passé avec succès :)")
    else:
        print("Echec du test :(")

pair = lambda a: a % 2 == 0
divise = lambda a, b: a % b == 0

test(pair, 7)
test(divise, 7, 3)