from character import *
from ennemy import *
from romainFunctions import *
from constantFight import *
import random

personnage = character()
windowInitialisation(personnage)

def combat() :
    
    while personnage.life :
        
        if ennemy.listEnnemy.count(0) == len(ennemy.listEnnemy) :
            victory()
            break
        
        redrawBoard(personnage)
        pygame.display.flip
        
        for mechant in ennemy.listEnnemy :
            if type(mechant) == ennemy :
                mechant.apparition = True
                if mechant.count != 0 :
                    mechant.count -= 1
        
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
        defeat()
        
    time.sleep(2)
    

def mob(etage) : 
    
    if etage == 1 : 
        listRandom = [[0,bat(1),bat(2),0,0],[bat(0),bat(1),bat(2),bat(3),0],[0,bat(1),bat(2),bat(3),0]]
        
    if etage == 2 :
        listRandom = [[0,spider(1),spider(2),spider(3),0],[0,spider(1),spider(2),0,0,0],[spider(0),spider(1),spider(2),spider(3),0],[0,0,spider(2),0,0]]
        
    if etage == 3:
        listRandom = [[0,0,gobelin(2),0,0],[0,gobelin(1),gobelin(2),gobelin(3),0],[0,gobelin(1),gobelin(2),0,0]]
    
    
    chosenListEnnemy = random.choice(listRandom)
    
    for x in range (0,5) :
        ennemy.listEnnemy[x] = chosenListEnnemy[x]
        
    combat()
    personnage.gold += 30

def boss(etage) :
    
    if etage == 1 :
        ennemy.listEnnemy[2] = vladimir(2)
        
    if etage == 2:
        ennemy.listEnnemy[2] = witch(2)
        
    if etage == 3:
        ennemy.listEnnemy[2] = ogre(2)
        
    if etage == 4:
        ennemy.listEnnemy[2] = Msmoke(2)
        
    combat()
    personnage.gold += 80

 

            
            
    
    
    
    
    
    
  
                
        


    

    
        
        
        
        
        
