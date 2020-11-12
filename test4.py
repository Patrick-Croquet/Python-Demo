def affiche_menu():
    print("Menu :")
    print("* Action 1")
    print("* Action 2")
affiche_menu()

def dire(texte):
    print('# ' + texte)
dire('Bonjour') # Affiche `# Bonjour`
dire('Au revoir') # Affiche `# Au revoir`

def addition(a, b):
    return a + b
somme=addition(10, 5) # Renvoie 15
# addition(10)
print(somme)
# addition()
print(addition(10, 5))

# def saluer(nom):
#    print('Bonjour ' + nom)

def saluer(nom = 'Visiteur'):
    print('Bonjour ' + nom)

#saluer('Clem')
saluer('Clem') # Affiche `Bonjour Clem`
saluer() # Affiche `Bonjour Visiteur`
