from character import *
from ennemy import * 


def askTarget(personnage) :
    
    loop = True
    
    while loop:
        
        targetChoice = input("""Quelle ennemi voulez vous ciblez ? """)
        
        try :
            targetChoice = int(targetChoice)
            ennemy.listEnnemy[targetChoice]
            assert not(ennemy.listEnnemy[targetChoice] == 0)
        
        except :
            print("Rentrez un nombre valide !")
            continue
    
        personnage.changeTarget(targetChoice)
        loop = False
        

def mobAttack(personnage) : 
    
    for i in ennemy.listEnnemy :
            if i != 0 : 
                i.dealDamage(personnage)
                if not personnage.life :
                    break