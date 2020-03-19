from character import *
from ennemy import *
from functions import *

personnage = character()

for x in range (0,5) :
    ennemy.listEnnemy[x] = bat(x)

windowInitialisation(personnage)

while personnage.life:
    
    if ennemy.listEnnemy.count(0) == len(ennemy.listEnnemy) :
            print("ET C'EST GAGNE !")
            break
    
    ennemy.presentationEnnemy()
    redrawBoard(personnage)
    choice = askAction()
    
    if choice == 1 :
        
        personnage.changeTarget(askTarget(personnage))
        personnage.dealDamage()
        mobAction(personnage)
                
        
    elif choice == 2 :
        
        personnage.useSkill()
        mobAction(personnage)
        
    elif choice == 3 :

        personnage.backpack.usePotion(personnage)  
        mobAction(personnage)
        
if not personnage.life :
    print("ET C'EST PERDU")
    
pygame.quit()
    

    
        
        
        
        
        