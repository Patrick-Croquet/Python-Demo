import transformers

def generate_product_description(model_name, 
                                 tonalite, 
                                 mots_cles, 
                                 capacite, 
                                 longueur_max):

  """
  Fonction pour générer une description de produit à partir d'un modèle de langage.

  Args:
    model_name (str): Nom du modèle de langage à utiliser.
    tonalite (str): Tonalité souhaitée de la description ("formelle" ou "informelle").
    mots_cles (list): Liste de mots clés à inclure dans la description.
    capacite (int): Capacité du produit en litres.
    longueur_max (int): Longueur maximale de la description en mots.

  Returns:
    str: Description de produit générée.
  """

  # Chargement du modèle
  model = transformers.AutoModelForConditionalGeneration.from_pretrained(model_name)

  # Définition du prompt
  prompt = f"Écrivez une description de produit pour un {mots_cles[0]} {tonalite} d'une capacité de {capacite} litres. Il est idéal pour la {mots_cles[1]} et le {mots_cles[2]}. (Limite de {longueur_max} mots)"

  # Génération de la description
  outputs = model.generate(prompt, max_length=longueur_max)

  # Décodage de la sortie
  description = outputs[0].decode("utf-8")

  return description

# Exemple d'utilisation
description = generate_product_description(model_name="facebook/bart-base",
                                         tonalite="informelle",
                                         mots_cles=["sac à dos", "randonnée", "camping"],
                                         capacite=20,
                                         longueur_max=100)

# Affichage de la description générée
print(description)