'''''''''''''''''''''''''''''''''
        CAPTEUR COULEUR
'''''''''''''''''''''''''''''''''
from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #                          ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

'''
Permet de renvoyer la couleur que le capteur capte
0 = rien/erreur // 1 = noir // 2 = bleu // 3 = vert // 4 = jaune // 5 = rouge // 6 = blanc // 7 = brun
-port : le port où le capteur est branché
return : la couleur
'''
def getColor(port):    
    try:
        BP.set_sensor_type(port, BP.SENSOR_TYPE.EV3_COLOR_COLOR)
        color = ["rien", "Noir", "Bleu", "Vert", "Jaune", "Rouge", "Blanc", "Brun"]
        value = BP.get_sensor(port)
        return color[value]               # print the color
    except brickpi3.SensorError as error:
        return error