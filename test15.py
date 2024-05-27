import random

# Liste des prénoms
prenoms = ["AOCHOL", "DAVID", "SEBASTIEN", "BENJAMIN", "BRUNO", "PIERRE", "JULIEN", "TIDGY", "AGATHE", "MOUNIA",
           "VIRGIL LEO", "CHLOE", "MARIE", "NAWAL", "RAYANNE", "SYLVAIN", "JULIANA", "NACERA", "ANDREW", "ENRIQUE"]

# Tirage aléatoire de deux prénoms
tirage = random.choices(prenoms, k=5)

# Affichage des prénoms tirés
print("Les prénoms tirés sont :", tirage)