from character import *
from ennemy import *
from romainFunctions import *
from constantFight import *
import functions as f
import random

personnage = character()
windowInitialisation(personnage)

#La fontion combat est celle appellé pour le déroulement d'un combat et des actions
def combat() :
    player = f.player

    while f.player.life : #Tant que le personnage est en vie
        
        if ennemy.listEnnemy.count(0) == len(ennemy.listEnnemy) :  #Si le nombre de 0 dans la liste vaut la taille de la liste
            victory()                                              #Cela signifie que tous les ennemis sont morts
            break
        
        #On redessine l'écran pour être sur que tout soit à jour
        redrawBoard(player)
        pygame.display.flip
        
        #Pour chaque ennemi, on lui permet d'attaquer au prochain tour, et on descend son compteur d'action si il est utilisé
        for mechant in ennemy.listEnnemy :
            if type(mechant) == ennemy :
                mechant.apparition = True
                if mechant.count != 0 :
                    mechant.count -= 1
        
        #On diminue aussi le cooldown de l'arme de 
        if f.player.weapon.cooldown != 0 :
            f.player.weapon.cooldown -= 1
        
        #On appelle la fonction de menu de sélection d'action
        choice = askAction()
        
        if choice == 1 :  #Si le joueur attaque avec son arme
            player.changeTarget(askTarget(player))   #On demande la cible à travers le menu
            player.dealDamage()   #Le personnage fait des dégâts à l'ennemi ciblé
            redrawBoard(player)    #On l'affiche à l'écran
            pygame.display.flip()
            mobAction(player)    #Pour finir, les mobs font leur action
            
        elif choice == 2 :    #Si le joueur utilise sa compétence spéciale
            player.useSkill()   #On utilise le pouvoir de la compétence spéciale
            mobAction(player)    #Les mobs font leur action
            
        elif choice == 3 :    #Si l'on choisit de se soigner
            player.backpack.usePotion(player)      #On se soigne
            redrawBoard(player)
            mobAction(player)    #Les mobs attaquent
    
    #A la sortie du while, on regarde si le joueur est mort : si oui, on dessine l'écran de mort
    #Sinon, cela signifie que le joueur en est sorti victorieux
    if not player.life :
        defeat()
    
    #On attend deux secondes afin de pouvoir apprécier l'écran de victoire/défaite
    time.sleep(2)
    
#Cette fonction est appellé lorsque le joueur marche sur une case ennemi
def mob(etage) : #Les ennemis dépendent de l'étage auquel on est
    
    #A chaque numéro d'étage est attribuée une liste contenant plusieurs possibilitées de combats 
    if etage == 1 :   
        listRandom = [[0,bat(1),bat(2),0,0],[bat(0),bat(1),bat(2),bat(3),0],[0,bat(1),bat(2),bat(3),0]]
        
    if etage == 2 :
        listRandom = [[0,spider(1),spider(2),spider(3),0],[0,spider(1),spider(2),0,0,0],[spider(0),spider(1),spider(2),spider(3),0],[0,0,spider(2),0,0]]
        
    if etage == 3:
        listRandom = [[0,0,gobelin(2),0,0],[0,gobelin(1),gobelin(2),gobelin(3),0],[0,gobelin(1),gobelin(2),0,0]]
    
    #On choisit un combat parmi ceux possibles
    chosenListEnnemy = random.choice(listRandom)
    
    #On attribue chaque élément de la liste choisie à une position dans la listEnnemi
    for x in range (0,5) :
        ennemy.listEnnemy[x] = chosenListEnnemy[x]
    
    #On lance le combat. A la fin de celui la, on gagne 30 golds
    combat()
    f.player.gold += 30

#Cette fonction est appellée quand on marche sur une case boss
def boss(etage) :
    
    #Suivant l'étage, le boss est différent
    if etage == 1 :
        ennemy.listEnnemy[2] = vladimir(2)
        
    if etage == 2:
        ennemy.listEnnemy[2] = witch(2)
        
    if etage == 3:
        ennemy.listEnnemy[2] = ogre(2)
        
    if etage == 4:
        ennemy.listEnnemy[2] = Msmoke(2)
    
    #On lance le combat, et on gagne 80 golds
    combat()
    f.player.gold += 80

 

            
            
    
    
    
    
    
    
  
                
        


    

    
        
        
        
        
        
