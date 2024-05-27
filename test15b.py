import random

# Liste des prénoms
prenoms = ["AOCHOL", "DAVID", "SEBASTIEN", "BENJAMIN", "BRUNO", "PIERRE", "JULIEN", "TIDGY", "AGATHE", "MOUNIA",
           "VIRGIL LEO", "CHLOE", "MARIE", "NAWAL", "RAYANNE", "SYLVAIN", "JULIANA", "NACERA", "ANDREW", "ENRIQUE"]

# Fonction pour lancer la roue et tirer un prénom
def lancer_roue():
    return random.choice(prenoms)

# Premier tirage
print("Premier tirage :", lancer_roue())

# Deuxième tirage
print("Deuxième tirage :", lancer_roue())