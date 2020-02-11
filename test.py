'''''''''''''''''''''''''''''''''
        PROGRAME PRINCIPAL
'''''''''''''''''''''''''''''''''
from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #                           ''

## Import de nos propre fichier pyhton
import moteursBrickPi as Moteur
import ColorSensor as Color
import TouchSensor
import display


## Import des librairies
import time,sys     # import the time library
import brickpi3 # import the BrickPi3 drivers
import random

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

'''''''''''''''''''''''''''''''''
        PORTS
'''''''''''''''''''''''''''''''''


portB = BP.PORT_B



'''''''''''''''''''''''''''''''''
        FONCTIONS
'''''''''''''''''''''''''''''''''


Moteur.Marche(portB,40)

time.sleep(2)

Moteur.Arret(portB)




            




       



