# Variable phrase en Caractère
# Variables Nb, i, j en Entier

# Debut
phrase = input("Entrez une phrase : ")  # Lire phrase
Nb = 0  # Nb ← 0
for i in range(0, len(phrase)):  # Pour i ← 1 à Len(phrase)
    if phrase[i] in "aeiouyàâéèêëîïôùûüAEIOUYÀÂÉÈÊËÎÏÔÙÛÜ":  # Si ((Mid(phrase, i, 1) = "a") OU (Mid(phrase, i, 1) = "e") OU ...)
        Nb += 1  # Nb ← Nb + 1
# FinSi
# i suivant
print("Cette phrase compte", Nb, "voyelles")  # Ecrire "Cette phrase compte ", Nb, " voyelles"
# Fin
