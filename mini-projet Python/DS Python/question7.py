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
Initialiser deux variables x1 et y1 valant 100 et 300 respectivement et une variable d pour que le robot dépose au point si la variable vaut 1.

"""
x1, y1 = 100, 300

d = 1

list1 = [-50, -30, 0, 50, 130]
list2 = [-50, 30, 0, 200, 20]
list3 = [0, 0, 1, 1, 0]


def action(x, y, d):
    """
    Déplacer le robot pour atteindre le point de coordonnées (x1, y1).
    """
    
    Time = RobotDeplacer(x1, y1)
    
    """
    Afficher le temps nécessaire pour effectuer cette action
    """
    print("le temps nécessaire pour effectuer cette action : " + str(Time) + " ms")
    
    
    if (d == 1):
        print("le robot dépose au point")
    else:
        print("le robot ne dépose pas au point")
        

"""
appeler la simulation "action".
"""        

action(x1,y1,d)    
"""
appeler la fin de la simulation.
"""

RobotFerm()






