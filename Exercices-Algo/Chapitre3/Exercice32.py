# VARIABLES
a = None  # Déclaration de la variable 'a' (sans initialisation)
b = None  # Déclaration de la variable 'b' (sans initialisation)

# Demander le premier nombre à l'utilisateur
a = float(input("Entrez le premier nombre : "))

# Demander le second nombre à l'utilisateur
b = float(input("Entrez le second nombre : "))

# Tester le signe des deux nombres et afficher le résultat
if a > 0 and b > 0:
    print("Le produit des deux nombres est positif")
elif a < 0 and b < 0:
    print("Le produit des deux nombres est positif")
else:
    print("Le produit des deux nombres est négatif")