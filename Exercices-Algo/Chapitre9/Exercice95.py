# Variable phrase en Caractère
# Variables Nb, i, j en Entier

# Début
phrase = input("Entrez une phrase : ")  # Lire phrase
print("Entrez le rang du caractère à supprimer : ") 
Nb = int(input())  # Lire Nb
L = len(phrase)  # L ← Len(phrase)
phrase = phrase[:Nb - 1] + phrase[Nb:]  # phrase ← Mid(phrase, 1, Nb – 1) & Mid(phrase, Nb + 1, L – Nb)
                                        # Mid(chaîne,n1,n2) : renvoie un extrait de la chaîne, commençant au caractère n1 et faisant n2 caractères de long.
print("La nouvelle phrase est : ", phrase)  # Ecrire "La nouvelle phrase est : ", phrase
# Fin
