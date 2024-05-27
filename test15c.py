import tkinter as tk
import random

# Liste des prénoms
prenoms = ["AOCHOL", "DAVID", "SEBASTIEN", "BENJAMIN", "BRUNO", "PIERRE", "JULIEN", "TIDGY", "AGATHE", "MOUNIA",
           "VIRGIL LEO", "CHLOE", "MARIE", "NAWAL", "RAYANNE", "SYLVAIN", "JULIANA", "NACERA", "ANDREW", "ENRIQUE"]

# Fonction pour tirer un prénom aléatoire
def tirer_prenom():
    return random.choice(prenoms)

# Fonction pour effectuer un tirage
def effectuer_tirage():
    # Premier tirage
    tirage1_label.config(text="Premier tirage : " + tirer_prenom())
    # Deuxième tirage
    tirage2_label.config(text="Deuxième tirage : " + tirer_prenom())

# Création de la fenêtre
root = tk.Tk()
root.title("Tirage de prénoms")

# Création des widgets
titre_label = tk.Label(root, text="Tirage de prénoms")
tirage1_label = tk.Label(root, text="")
tirage2_label = tk.Label(root, text="")
tirage_button = tk.Button(root, text="Effectuer un tirage", command=effectuer_tirage)

# Placement des widgets dans la fenêtre
titre_label.pack()
tirage1_label.pack()
tirage2_label.pack()
tirage_button.pack()

# Lancement de la boucle principale
root.mainloop()