# Variables Nom, Prenom, Mail, Ville

# Début
Nom = input("Entrez le nom : ") #Lire Nom
Prenom = input("Entrez le prenom : ") #Lire Prenom
Mail = input("Entrez le mail : ") #Lire Mail
Ville = input("Entrez la ville : ") #Lire Ville
ligne = Nom.ljust(20) + Prenom.ljust(17) + Mail.ljust(25) + Ville.ljust(30)
with open("carnet.txt", "+a") as file:
    file.write(ligne + "\n")
# Fin