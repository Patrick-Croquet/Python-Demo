# Exemple de procédure principale appelant deux sous-procédures pour afficher un message
def afficher_message():
    print("Message de la procédure principale.")
    sous_procedure1()
    sous_procedure2()

def sous_procedure1():
    print("Message de la sous-procédure 1.")

def sous_procedure2():
    print("Message de la sous-procédure 2.")

# Appel de la sous-procédure 1 et de la sous-procédure 2 à partir de la procédure principale
afficher_message()