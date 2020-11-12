# -*- coding: cp1252 -*-
# tables.py par maxpeg0705

# Met du vide dans la variable numero
numero = ''

# Tant que numero est vide
while (numero == ''):
                # Stocke dans la variable numéro la réponse de l'utilisateur
                try:
                    numero = int(input('Quelle table de multiplication ? (entre 1 et 10) : '))
                # Si il y a une erreur !!
                except:
                    print ('Veuillez entrer un chiffre !!')

# Tant que numero est plus petit que 1
while (numero < 1):
                   print ('Veuillez entrer un chiffre compris entre 1 et 10 !!')
                   numero = int(input('Quelle table de multiplication ? (entre 1 et 10) : '))

# Tant que numero est plus grand que 10
while (numero > 10):
                   print ('Veuillez entrer un chiffre compris entre 1 et 10 !!')
                   numero = int(input('Quelle table de multiplication ? (entre 1 et 10) : '))

# Autrement on affiche
else :
                # Met une ligne vide
                print('')
                a,b,c = numero,2,numero
                # Pour afficher seulement 10 resultats
                maxi = numero * 10
                # Tant que a ne depasse pas maxi
                while (a <= maxi) :
                    print (a)
                    a = c * b
                    b = b + 1