from character import *
from ennemy import *

personnage = character(hp = 10030)
gobelin = ennemy(2)
squelette = ennemy(1,name = 'Skeleton')

while personnage.life: 
    ennemy.presentationEnnemy()
    choice = input("""Que voulez vous faire ? 1 - Attaquer / 2 - Utiliser la compétence spéciale / 3 - Ouvrir le sac à dos """)
    if choice == '1' :
        
        askTarget(personnage)
        personnage.dealDamage()
        mobAttack(personnage)
                
        
    elif choice == '2' :
        
        personnage.useSkill()
        mobAttack(personnage)
        
    elif choice == '3' :

        personnage.backpack.usePotion(personnage)  
        mobAttack(personnage)          
    
    else : 
        
        print("Rentrez un nombre valide !")
        
print("ET C'EST PERDU")
        
        
        
        
        