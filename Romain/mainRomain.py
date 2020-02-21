from character import *
from ennemy import *
from functions import *

personnage = character(hp = 100)

vladimir = vladimir(2)

while personnage.life:
    
    if ennemy.listEnnemy.count(0) == len(ennemy.listEnnemy) :
        print("ET C'EST GAGNE !")
        break
    
    ennemy.presentationEnnemy()
    choice = input("""Que voulez vous faire ? 1 - Attaquer / 2 - Utiliser la compétence spéciale / 3 - Ouvrir le sac à dos """)
    
    if choice == '1' :
        
        askTarget(personnage)
        personnage.dealDamage()
        mobAction(personnage)
                
        
    elif choice == '2' :
        
        personnage.useSkill()
        mobAction(personnage)
        
    elif choice == '3' :

        personnage.backpack.usePotion(personnage)  
        mobAction(personnage)          
    
    else : 
        
        print("Rentrez un nombre valide !")
        
if not personnage.life :
    print("ET C'EST PERDU")
    

    
        
        
        
        
        