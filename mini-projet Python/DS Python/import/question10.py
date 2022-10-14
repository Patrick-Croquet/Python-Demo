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

x0 = 0
y0 = 0
RobotInit(x0, y0)

with open("grilles/grille2.txt", "r") as fichier:
    for line in fichier:
       if "format : " in line:
           data = line.split()
print(data[2])

coord = data[2].split('*')
print(coord)
"""
Initialiser deux variables n et m valant 3 et 4 respectivement.

"""

n, m = coord[0], coord[1]

print(str(n) +" lignes et " + str(m) + " colonnes")


"""
Appeler la fin de la simulation.
"""

RobotFerm()






