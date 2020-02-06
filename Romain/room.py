from character import *
from ennemy import *

class room :
    
    def __init__ (self,character,ennemy0,ennemy1,ennemy2,ennemy3,ennemy4):
        self.character = character
        self.listeEnnemy = list(ennemy)
        
    def presentation(self) :
        print("Le gentil est {0} et le(s) méchant(s) est/sont ".format(self.character.name))
        
    