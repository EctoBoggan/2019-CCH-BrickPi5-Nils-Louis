'''''''''''''''''''''''''''''''''
        CAPTEUR COULEUR
'''''''''''''''''''''''''''''''''
#Classe qui décrit un capteur de couleur BrickPi

from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #
from collections import Counter       # permet de compter les occurences
import statistics 

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

'''
Permet de renvoyer la couleur que le capteur capte
0 = rien/erreur
1 = noir
2 = bleu
3 = vert
4 = jaune
5 = rouge
6 = blanc
7 = brun
-port : le port où le capteur est branché
return : la couleur
'''
def getColor(port):
    listColor = []
    try:
        for i in range(9):
            BP.set_sensor_type(port, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
            color = ["Rien", "Noir", "Bleu", "Vert", "Jaune", "Rouge", "Blanc", "Brun"]
            value = BP.get_sensor(port)
            return color[value]
    except brickpi3.SensorError as error:
        getColor(port)
        
'''
Fonction trop bien tapé à la main qui ne marche que quand elle le souhaite
-list_couleur : liste de couleurs précédement captées
Retourne la couleur la plus présente dans la liste, ou peut-être pas.
'''
'''
def most_frequent(list_couleur):
    rouge = 0
    bleu = 0
    jaune = 0
    vert = 0
    blanc = 0
    noir = 0
    rien = 0
    
    for couleur in list_couleur:
        if couleur == "Rouge":
            rouge +=1
        elif couleur == "Bleu":
            bleu += 1
        elif couleur == "Jaune":
            jaune += 1
        elif couleur == "Vert":
            vert += 1
        elif couleur == "Blanc":
            blanc += 1
        elif couleur == "Noir":
            noir += 1
        else:
            rien += 1
            
    most_frequent_color = "gpalu"
    tempnum = 0
    if rouge >  bleu:
        most_frequent_color = "Rouge"
        tempnum = rouge
    else:
        most_frequent_color = "Bleu"
        tempnum = bleu
    if tempnum < jaune:
        most_frequent_color = "Jaune"
        tempnum = jaune
    elif tempnum < vert:
        most_frequent_color = "Vert"
        tempnum = vert
    elif tempnum < blanc:
        most_frequent_color = "Blanc"
        tempnum = blanc
    elif tempnum < noir:
        most_frequent_color = "Noir"
    else:
        most_frequent_color = "Rien"
    
    return most_frequent_color
'''