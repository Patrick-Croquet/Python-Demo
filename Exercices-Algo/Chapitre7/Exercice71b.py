def sont_consecutifs(tab):
    # Vérifie si tous les éléments du tableau sont consécutifs
    return all(tab[i] + 1 == tab[i+1] for i in range(len(tab) - 1))

def main():
    # Saisie des valeurs et rangement dans un tableau
    valeurs = []
    while True:
        valeur = input("Entrez une valeur (ou 'q' pour terminer) : ")
        if valeur.lower() == 'q':
            break
        try:
            valeurs.append(int(valeur))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Vérification si les éléments du tableau sont consécutifs
    if sont_consecutifs(sorted(valeurs)):
        print("Les éléments du tableau sont tous consécutifs.")
    else:
        print("Les éléments du tableau ne sont pas tous consécutifs.")

if __name__ == "__main__":
    main()