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
    
def RobotDeposer(t):
    # le robot dépose à sa position actuelle
    # renvoie le temps de l'opération
    turtle.write(t,align='center',font=("Arial", 10, "normal"))
    return(2)
    
#%% Script

"""
zone du code à remplir
"""

"""
Initialiser le robot en position (0,0)
"""

x0 = -150
y0 = -150
RobotInit(x0, y0)

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
listd = []

"""
Initialiser une matrice (type numpy.array) remplie de 0 de taille n*m.
"""

matrice = np.zeros((n,m))
size = 80

print (matrice)

   
for j in range(0,n):
    if (j%2 == 0):       # si je suis sur une ligne impaire je parcours de gauche à droite. Attention le premier élément d'un tableau est à l'indice 0
        for i in range(0,m,1):
            matrice[j,i] = 1
            print(((n-1)-j)*size,i*size)
            listy.append(((n-1)-j)*size)
            listx.append(i*size)
            listd.append(1)

    else:
        for i in range(m-1,-1,-1): # si je suis sur une ligne paire je parcours de droite à gauche. 
            matrice[j,i] = 1 
            print(((n-1)-j)*size,i*size)
            listy.append(((n-1)-j)*size)
            listx.append(i*size)
            listd.append(1)
            

print (matrice)


"""
Listes des coordonnées x et y 
"""

print(listx)
print(listy)

"""
Liste du temps nécessire à la dépose des points
"""
listtd = []

TotalTime = 0

def action(x, y):
    """
    Déplacer le robot pour atteindre le point de coordonnées (x1, y1).
    """
    
    Time = RobotDeplacer(x, y)
    Time += RobotDeposer(round(Time,2))
        
    """
        Afficher le temps nécessaire pour effectuer cette action (déplacement + dépose)
    """
        
    print("le temps nécessaire pour effectuer cette action (déplacement + dépose) : " + str(Time) + " ms")

        
    listtd.append(Time)
"""
appeler la simulation "action".
"""        

for i in range(m*n):
    x = listx[i]
    y = listy[i]
    d = listd[i]
    
    action(x,y)

print(listtd)

"""
Temps total nécessaire pour effectuer ces opérations
"""

for i in range(len(listtd)):
    TotalTime += listtd[i]
    
print("Temps total nécessaire pour effectuer ces opérations : " + str(TotalTime))

"""
Appeler la fin de la simulation.
"""

RobotFerm()






