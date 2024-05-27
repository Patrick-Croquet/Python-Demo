# Exemple de variables locales et globales
variable_globale = 10

def fonction():
    variable_locale = 5
    print("Variable locale dans la fonction :", variable_locale)
    print("Variable globale dans la fonction :", variable_globale)

fonction()
print("Variable globale en dehors de la fonction :", variable_globale)
# La variable_locale n'est pas accessible en dehors de la fonction
# print("Variable locale en dehors de la fonction :", variable_locale) # Cela lèverait une erreur
