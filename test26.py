class Bottin:
    def __init__(self, nom, prenom, tel, mail):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail

Mespotes = []

with open("Exemple.txt", "r") as fichier:
    i = -1
    while True:
        i += 1
        line = fichier.readline()
        if not line:  # Vérifie si on a atteint la fin du fichier
            break
        # Extraction des données de la ligne selon la structure Bottin
        nom = line[0:20].strip()
        prenom = line[20:35].strip()
        tel = line[35:45].strip()
        mail = line[45:65].strip()
        # Création d'un nouvel objet Bottin et ajout à la liste Mespotes
        Mespotes.append(Bottin(nom, prenom, tel, mail))

print(Mespotes[0])