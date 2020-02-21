from character import *


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
        

def mobAction(personnage) : 
    
    for mechant in ennemy.listEnnemy :
            if mechant != 0 :
                mechant.action(personnage)
                if not personnage.life :
                    break
                
def gobelin(position) :
    
    return ennemy(position)

def skeleton(position) :
    
    return ennemy(position,"Squelette",7,40)

def troll(position) :
    
    return ennemy(position,"Troll",20,50)

def bat(position) :
    
    return ennemy(position,"Chauve-souris",5,10)

def vladimir(position) :
    
    return ennemy(position,"Comte Vladimir",15,100,'Bat')
    