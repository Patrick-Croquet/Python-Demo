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

with open("grilles/grille2.txt", "r") as fichier:
    for line in fichier:
       if "format : " in line:
           line1 = line.split()
       if "taille case : " in line:
           line2 = line.split()
       if "depart : " in line:
           line3 = line.split()

"""           
print(line1[2])
print(line2[2])
print(line3[2])
"""

coord = line1[2].split('*')
size = line2[3].split('*')
departure = line3[2].split(',')

print(coord)
print(size)
print(departure)

"""
Initialiser deux variables n et m avec les coordonnées des fichiers grille.txt

"""

n, m = int(coord[0]), int(coord[1])

print(str(n) +" lignes et " + str(m) + " colonnes")

"""
Initialiser le robot en position de départ
"""

x0 = 0
y0 = 0
RobotInit(x0, y0)

"""
Initialiser une matrice (type numpy.array) remplie de 0 de taille n*m.
"""

matrice = np.zeros((n,m))

print (matrice)

"""
Appeler la fin de la simulation.
"""

RobotFerm()






