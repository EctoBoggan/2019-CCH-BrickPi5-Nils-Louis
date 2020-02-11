'''''''''''''''''''''''''''''''''
        MOTEUR BRICKPI
'''''''''''''''''''''''''''''''''
from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #                          ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

import TouchSensor

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

'''
-Met en marche un moteur-
portMoteur : le port du moteur que l'on veut mettre en marche
vitesse : vitesse à laquelle l'on veut que le moteur tourne (de 0 à 100)
'''
def Marche(port,vitesse):
    
    BP.set_motor_power(port, vitesse)

'''
-Met en arrêt un moteur-
portMoteur : le port du moteur que l'on veut mettre en arrêt
'''
def Arret(port):
    
    BP.set_motor_power(port, 0)

'''
-Fait reculer un moteur jusqu'à ce que le poussoir soit poussé
portTouch : port du poussoir
portMoteur : port du moteur
'''
def Retour(portTouch,portMoteur):
    while not TouchSensor.estAppuyé(portTouch):        
        Marche(portMoteur,-20)            
    else:
        Arret(portMoteur)