# -*- coding: utf-8 -*-
"""
Script permettant au robot turtle de suivre les instructions contenues dans 
un fichier question6.py

Code à remplir dans la section script

"""
#%% import

import turtle
import numpy as np

#%% Definition des fonctions de base du robot

def RobotInit(x,y,largeur=950,hauteur=800):
    # initialisation du robot
    # x et y les coordonnées du point de départ
    turtle.setup(largeur,hauteur) # creation de la fenetre
    # positionnement au point de départ :
    turtle.penup()
    turtle.goto(x,y)
    global ptAct, dirAct
    ptAct=np.array([x,y])
    dirAct=np.array([1,0])
    turtle.pendown()

def RobotFerm():
    # à appeler pour mettre fin au déplacement du robot
    # n'oubliez pas d'appeler cette fonction à la fin de votre script !
    turtle.exitonclick()
    turtle.bye()

def RobotDeplacer(x,y):
    # deplacer le robot à partir d'instructions
    # x et y les coordonnées du point à atteindre
    # renvoie le temps de parcours 
    global ptAct, dirAct
    dirN=np.array([x,y])-ptAct
    distance=np.sqrt(dirN[0]**2+dirN[1]**2)
    angle=np.arctan2(dirN[1],dirN[0])-np.arctan2(dirAct[1],dirAct[0])
    angle=angle*180/np.pi
    if angle>180:
        angle=angle-360
    elif angle<-180:
        angle=360+angle
    turtle.left(angle)
    turtle.forward(distance)
    dirAct=dirN
    ptAct=np.array([x,y])
    return (distance/25+angle/180)
    
def RobotDeposer():
    # le robot dépose à sa position actuelle
    # renvoie le temps de l'opération
    turtle.write('X',align='center',font=("Arial", 10, "normal"))
    return(2)
    
#%% Script

"""
zone du code à remplir
"""

"""
Initialiser le robot en position (0,0)
"""

RobotInit(0, 0)

"""
Initialiser deux variables n et m valant 3 et 4 respectivement.

"""

n = int(input("Entrer le nombre de lignes :"))
m = int(input("Entrer le nombre de colonnes :"))

print(str(n) +" lignes et " + str(m) + " colonnes")

"""
Listes des coordonnées x et y 
"""

listx = []
listy = []

"""
Initialiser une matrice (type numpy.array) remplie de 0 de taille n*m.
"""

matrice = np.zeros((n,m))

print (matrice)

   
for j in range(0,n):
    if (j%2 == 0):       # si je suis sur une ligne impaire je parcours de gauche à droite. Attention le premier élément d'un tableau est à l'indice 0
        for i in range(0,m,1):
            matrice[j,i] = 1
            print(((n-1)-j)*50,i*50)
            listy.append(((n-1)-j)*50)
            listx.append(i*50)

    else:
        for i in range(m-1,-1,-1): # si je suis sur une ligne paire je parcours de droite à gauche. 
            matrice[j,i] = 1 
            print(((n-1)-j)*50,i*50)
            listy.append(((n-1)-j)*50)
            listx.append(i*50)
            
        


print (matrice)


"""
Listes des coordonnées x et y 
"""

print(listx)
print(listy)

"""
Appeler la fin de la simulation.
"""

RobotFerm()






