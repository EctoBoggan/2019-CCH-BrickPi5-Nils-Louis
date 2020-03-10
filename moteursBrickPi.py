'''''''''''''''''''''''''''''''''
        MOTEUR BRICKPI
'''''''''''''''''''''''''''''''''
#Classe qui décrit un moteurBrickPi

from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #                          ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

import TouchSensor

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

'''
-Met en marche un moteur-
port : le port du moteur que l'on veut mettre en marche
vitesse : vitesse à laquelle l'on veut que le moteur tourne (de 0 à 100)
'''
def Marche(port,vitesse):    
        BP.set_motor_power(port, (vitesse * -1))

'''
-Met en marche un môteur
port : le port du moteur que l'n veut mettre en marche
vitesse : vitesse à la quelle l'on veut que le moteur tourne ( de 0 à 100)
encoder : jusqu'à quel encoder l'on souhait que le moteur tourne (1 encoder = 1°)
MoteurY : vitesse + , encoder -
MoteurX : vitesse + , encoder +
'''
def MarcheEncoder(port,vitesse,encoder):
    #MoteurY
    if encoder < 0:
        while BP.get_motor_encoder(port) > encoder:
            Marche(port,vitesse)
    #MoteurX
    else:
        while BP.get_motor_encoder(port) < encoder:
            Marche(port,vitesse)    
        
    Arret(port)
    
'''
-Renvoie un moteur à sa position d'origine
port : port moteur
(va ]être utile au moteurX car il n'a pas de butée)
'''
    
def RetourZero(port):       
    while BP.get_motor_encoder(port) > 0:
        Marche(port,15)
    Arret(port)
    BP.offset_motor_encoder(port,BP.get_motor_encoder(port))

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
        Marche(portMoteur,-25)            
    else:
        Arret(portMoteur)
        BP.offset_motor_encoder(portMoteur,BP.get_motor_encoder(portMoteur))

'''
-Remet l'encoder du moteur à zéro
port : port moteur
'''
def Reset(port):
    BP.offset_motor_encoder(port,BP.get_motor_encoder(port))


'''
-Fait bouger le robot mannuellement à l'aide du bouton et du bumper
-Moteur : moteur
-bumper : bumper
-bouton : bouton
'''
def moteurManuel(MoteurX,bumper,bouton):
    while True:
        
        if(TouchSensor.estAppuyé(bouton) == True):
            Marche(MoteurX, 30)
        else:
            Arret(MoteurX)
            
        if(TouchSensor.estAppuyé(bumper) == True):
            Marche(MoteurX, -30)
        else:
            Arret(MoteurX)

    