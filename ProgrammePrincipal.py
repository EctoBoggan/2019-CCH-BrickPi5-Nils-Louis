'''''''''''''''''''''''''''''''''
        PROGRAME PRINCIPAL
'''''''''''''''''''''''''''''''''
#Programme principal du robot jouant à masterMind

from __future__ import print_function # utiliser Py3 mais le rendre compatible avec Py2
from __future__ import division       #                           ''

## Import de nos propre fichier pyhton
import moteursBrickPi as Moteur
import ColorSensor as Color
import TouchSensor as Touch
import display


## Import des librairies
import time,sys     # import the time library
import brickpi3 # import the BrickPi3 drivers
import random

BP = brickpi3.BrickPi3() # Créer une instance de la classe BrickPi3. BP sera l'objet de cette classe.

'''''''''''''''''''''''''''''''''
        PORTS
'''''''''''''''''''''''''''''''''
#Capteurs
bumper = BP.PORT_2
bouton = BP.PORT_3
captColor = BP.PORT_1

#Moteurs
portMoteurY = BP.PORT_C
portMoteurX = BP.PORT_B


'''''''''''''''''''''''''''''''''
        FONCTIONS
        préciser où les fonction sont utilisée // plus de précision
'''''''''''''''''''''''''''''''''

'''
Créé une listes de 4 couleurs aléatoires
return : une liste de 4 couleurs aléatoires
changement : ajouter 4 en nom de fonction et définir les couleurs en constante disponnible // ajouter un param int pour choisir un nombre de couleur
'''
def tirageCouleur():
    couleursDispo = ["blanc","noir","rouge","bleu","vert","jaune"]
    tirage = []
    for i in range(4):
        tirage.append(random.choice(couleursDispo))
    return tirage

        
'''
Fait clignoter régulièrement le texte
(2eme solution : faire appara]ître le text, retourner la fonction, puis enleve rle texte via une autre place)
'''
def LCDclignotement():
    time.sleep(1)
    display.setText(" ")
    time.sleep(0.2)

'''
Permet au robot de recalibrer sa position en retournant à son point de départ
'''
def positionInitiale():
    'Position intiale Y'
    Moteur.Retour(bumper,portMoteurY)
    time.sleep(1)
    
    'position initiale X'
    Moteur.RetourZero(portMoteurX)

'''
Déplace le capteur couleur jusqu'à la prochaine couleur
-playCouleur (de la 1ère à la 4ème place)
1ère = 0
2ème = 110
3ème = 220
4ème = 330
'''
def prochaineCouleur(placeCouleur):
    Moteur.MarcheEncoder(portMoteurX,-15,125*(placeCouleur-1))


'''''''''''''''''''''''''''''''''
        MAIN PROGRAM
'''''''''''''''''''''''''''''''''
Moteur.Reset(portMoteurY)
Moteur.Reset(portMoteurX)

while True:
    #Commencer la partie lors de l'appui du bouton    
    if (Touch.estAppuyé(bouton)):
        
        #Le robot effectue son tirage
        tirageRobot = list(tirageCouleur())
        for couleur in range(4):
            print(tirageRobot[couleur])        
        
        encoder = -59
        #Commencer les dix tours
        for tour in range(10):
            positionInitiale()
            Moteur.MarcheEncoder(portMoteurY,20,(encoder * (tour+2))) #Avance à la ligne correspondante au tour
            time.sleep(1)
            #Check les 4 couleurs
            for placeCouleur in range(1,5): # de la place 1 à la place 4
                prochaineCouleur(placeCouleur)
                time.sleep(0.1)
                #Enregistrer la couleur
                print(Color.getColor(captColor))
                time.sleep(0.1)
            Moteur.RetourZero(portMoteurX)
            #A la fin, retour à la place initiale
        positionInitiale()
    
            