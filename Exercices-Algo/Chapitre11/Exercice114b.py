def purge(chaine, caractere):
    nouvelle_chaine = ""
    for char in chaine:
        if char != caractere:
            nouvelle_chaine += char
    return nouvelle_chaine

resultat = purge("Bonjour", "o")
print(resultat) 