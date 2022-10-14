# -*- coding: utf-8 -*-
"""
Script permettant au robot turtle de suivre les instructions contenues dans 
un fichier .txt

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

RobotInit(0, 0)

S = 1

x1 = 100 
y1 = 300


Time = RobotDeplacer(x1, y1)
totalTime = 0

"""
print(T)

x2 = -50 
y2 = -50


T = RobotDeplacer(x2, y2)

print(T)



def V (x, y, d):
    
    T = RobotDeplacer(x, y)

    if d == 1:
        RobotDeposer()
    
    return(T)
"""    
    
E1 = [-50, -30, 0, 50, 130]
V1 = [-50, 30, 0, 200, 20]
E2 = [0, 0, 1, 1, 0]

"Ajout de la nouvelle liste"

N0 = []

for i in range(5):
    x = E1[i]
    y = V1[i]

    Time = RobotDeplacer(x, y)   
    print(Time)
    totalTime += Time
    
    d = E2[i]
    print(d)
    
print(totalTime)

 
RobotFerm()

    

    
    