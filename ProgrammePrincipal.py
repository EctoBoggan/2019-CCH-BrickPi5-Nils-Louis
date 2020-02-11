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

portTouch = BP.PORT_2
portMoteur = BP.PORT_C

'''''''''''''''''''''''''''''''''
        FONCTIONS
'''''''''''''''''''''''''''''''''

'''
Créé une listes de 4 couleurs aléatoires
return : une liste de 4 couleurs aléatoires
'''
def tirageCouleur():
    couleursDispo = ["blanc","noir","rouge","bleu","vert","jaune"]
    tirage = []
    for i in range(4):
        tirage.append(random.choice(couleursDispo))
    return tirage

'''
Lance le début d'un nouveau tour en annoncant le numéro du tour et en demandant de jouer
-tour : numéro du tour actuel
'''
def débutTour(tour):
    display.setText("Tour " + str(tour+1))
    time.sleep(5)
    while not(TouchSensor.estAppuyé(portTouch)):
        display.setText("lol" + str(tour+1))
        time.sleep(2)

'''''''''''''''''''''''''''''''''
        MAIN PROGRAM
'''''''''''''''''''''''''''''''''
changerLCD = True

while True:
    #Commencer la partie lors de l'appui du bouton    
    
    if (TouchSensor.estAppuyé(portTouch)):
        
        #Le robot effectue son tirage
        monTirage = list(tirageCouleur())
        for couleur in range(4):
            print(monTirage[couleur])
        
        #Commencer les dix tours
        for tour in range(10):
            débutTour(tour)
            
    else:
        if(changerLCD):
            changerLCD = False
            display.setText("Appuyez sur bouton")
            display.setRGB(11,10,12)


            




       


