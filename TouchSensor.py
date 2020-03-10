'''''''''''''''''''''''''''''''''
        TOUCH SENSOR
'''''''''''''''''''''''''''''''''
#Classe qui décrit un capteur de pression

from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #                          ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.TOUCH) #Définition du capteur
BP.set_sensor_type(BP.PORT_3, BP.SENSOR_TYPE.TOUCH) #Définition du capteur

'''
-Test si le TouchSensor est appuyé ou non-
Return : True = Appuyé // False = Pas appuyé
'''
def estAppuyé(port):
    if(BP.get_sensor(port) == 1):
        return True
    else:
        return False