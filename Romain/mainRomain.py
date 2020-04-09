from character import *
from ennemy import *
from functions import *

personnage = character()

for x in range (0,5) :
    ennemy.listEnnemy[x] = spider(x)

windowInitialisation(personnage)

while personnage.life:
    
    if ennemy.listEnnemy.count(0) == len(ennemy.listEnnemy) :
            print("ET C'EST GAGNE !")
            victory()
            break
    
    redrawBoard(personnage)
    pygame.display.flip()
    
    for mechant in ennemy.listEnnemy :
        if type(mechant) == ennemy :
            mechant.apparition = True
    
    if personnage.weapon.cooldown != 0 :
        personnage.weapon.cooldown -= 1
    
    choice = askAction()
    
    if choice == 1 :
        
        personnage.changeTarget(askTarget(personnage))
        personnage.dealDamage()
        redrawBoard(personnage)
        pygame.display.flip()
        mobAction(personnage)
                
        
    elif choice == 2 :
        
        personnage.useSkill()
        mobAction(personnage)
        
    elif choice == 3 :

        personnage.backpack.usePotion(personnage)  
        redrawBoard(personnage)
        mobAction(personnage)
        
if not personnage.life :
    print("ET C'EST PERDU")
    defeat()
    
pygame.quit()
    

    
        
        
        
        
        