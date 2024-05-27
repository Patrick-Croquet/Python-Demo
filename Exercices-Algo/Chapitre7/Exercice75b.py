def recherche_dichotomique(mot, dico):
    sup = len(dico) - 1
    inf = 0
    fini = False
    
    while not fini:
        comp = (sup + inf) // 2
        if mot < dico[comp]:
            sup = comp - 1
        else:
            inf = comp + 1
        
        fini = mot == dico[comp] or sup < inf

    if mot == dico[comp]:
        print("Le mot existe")
    else:
        print("Il n'existe pas")

# Exemple d'utilisation
dictionnaire = ["chat", "chien", "lapin", "lion", "tigre"]
mot_a_chercher = input("Entrez le mot à vérifier : ")
recherche_dichotomique(mot_a_chercher, dictionnaire)