# Exemple d'utilisation
dico = ["chat", "chien", "lapin", "lion", "tigre"]
mot = input("Entrez le mot à vérifier : ")

sup = len(dico) - 1
inf = 0
fini = False

while not fini:
    compteur = (sup + inf) // 2
    if mot < dico[compteur]:
        sup = compteur - 1
    elif mot > dico[compteur]:
        inf = compteur + 1
    else :
        break    
    fini = mot == dico[compteur] or sup < inf



if fini :
    print("Il n'existe pas")    
else:
    print("Le mot existe")