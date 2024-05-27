# VARIABLES
age = None  # Déclaration de la variable 'age' (sans initialisation)

# Demander l'âge de l'enfant à l'utilisateur
age = int(input("Entrez l'âge de l'enfant : "))

# Déterminer la catégorie de l'enfant en fonction de son âge
if age >= 12:
    categorie = "Cadet"
elif age >= 10:
    categorie = "Minime"
elif age >= 8:
    categorie = "Pupille"
elif age >= 6:
    categorie = "Poussin"
else:
    categorie = "Non classé"  # On peut ajouter une catégorie par défaut ici

# Afficher la catégorie de l'enfant
print(f"L'enfant est dans la catégorie {categorie}.")