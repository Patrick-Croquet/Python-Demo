import random

# Définition des variables
NB_COULEURS = 4
LONGUEUR_COMBINAISON = 4
NB_ESSAIS_MAX = 10

# Couleurs possibles
couleurs = [1, 2, 3, 4]

def generer_combinaison_secrete():
  """Génère une combinaison secrète aléatoire."""
  combinaison_secrete = []
  for _ in range(LONGUEUR_COMBINAISON):
    combinaison_secrete.append(random.choice(couleurs))
  return combinaison_secrete

def afficher_combinaison(combinaison):
  """Affiche une combinaison de couleurs."""
  for couleur in combinaison:
    print(couleur, end=" ")
  print()

def verifier_proposition(combinaison_secrete, proposition_joueur):
  """Vérifie la proposition du joueur et retourne le nombre de pions bien placés et mal placés."""
  nb_pions_bien_places = 0
  nb_pions_mal_places = 0
  combinaison_joueur_marque = [0] * LONGUEUR_COMBINAISON

  # Pions bien placés
  for i in range(LONGUEUR_COMBINAISON):
    if combinaison_secrete[i] == proposition_joueur[i]:
      nb_pions_bien_places += 1
      combinaison_joueur_marque[i] = 1

  # Pions mal placés
  for i in range(LONGUEUR_COMBINAISON):
    if combinaison_joueur_marque[i] == 0:
      for j in range(LONGUEUR_COMBINAISON):
        if combinaison_secrete[j] == proposition_joueur[i] and combinaison_joueur_marque[j] == 0:
          nb_pions_mal_places += 1
          combinaison_joueur_marque[j] = 1
          break

  return nb_pions_bien_places, nb_pions_mal_places

def jouer_manche(combinaison_secrete):
  """Joue une manche du jeu."""
  nb_essais = 0
  proposition_joueur = None

  while nb_essais < NB_ESSAIS_MAX and proposition_joueur != combinaison_secrete:
    # Proposition du joueur
    proposition_joueur = []
    for i in range(LONGUEUR_COMBINAISON):
      while True:
        try:
          couleur = int(input(f"Saisissez la couleur {i + 1} (1, 2, 3, 4) : "))
          if 1 <= couleur <= NB_COULEURS:
            break
          else:
            print("Erreur : Saisie incorrecte. Veuillez saisir une valeur entre 1 et 4.")
        except ValueError:
          print("Erreur : Saisie incorrecte. Veuillez saisir un nombre entier.")
      proposition_joueur.append(couleur)

    # Évaluation de la proposition
    nb_pions_bien_places, nb_pions_mal_places = verifier_proposition(combinaison_secrete, proposition_joueur)

    # Affichage du résultat
    print(f"{nb_pions_bien_places} pion(s) bien placé(s).")
    print(f"{nb_pions_mal_places} pion(s) de la bonne couleur mais mal placé(s).")

    nb_essais += 1

  if proposition_joueur == combinaison_secrete:
    print("Manche gagnée !")
  else:
    print("Manche perdue !")
    afficher_combinaison(combinaison_secrete)

def jouer():
  """Fonction principale du jeu."""
  # Nombre de manches
  while True:
    try:
      nb_manches = int(input("Combien de manches souhaitez-vous jouer ? "))
      if nb_manches > 0:
        break
      else:
        print("Erreur : Veuillez saisir un nombre de manches positif.")
    except ValueError:
      print("Erreur : Saisie incorrecte. Veuillez saisir un nombre entier.")

  # Boucle principale du jeu
  for manche in range(1, nb_manches + 1):
    print(f"\nManche {manche} :")
    combinaison_secrete = generer_combinaison_secrete()
    jouer_manche(combinaison_secrete)

if __name__ == "__main__":
  jouer() 
