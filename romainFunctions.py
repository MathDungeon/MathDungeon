from character import *
from constantFight import *
from random import randint
from constants import *
import functions as f
import time
import pygame

"""
Ce fichier sert à créer des fonctions qui permettent de simplifier le code, lui faire gagner en lisibilité 
    et de ne pas réécrire les mêmes portions plusieurs fois
"""



"""
Tout d'abord, trois fonctions permettent de dessiner plusieurs choses sur la fenêtre de jeu
"""

#Cette fonction sert à dessiner toute la fenêtre graphique, avec le curseur jaune de sélection des ennemis
#Elle est utilisée lorsque l'on choisit l'ennemi à cibler, afin de voir le curseur dessiné à chaque fois que l'on change de cible
def drawEnnemyCursor(ennemyCursor) :
    
    global window
    #Pour le premier dessinage global, je vais commenter à quoi sert chaque phrase
    window.blit(spr_dungeon,(0,0))    #Affiche le fond d'écran, le dongon 
    window.blit(spr_selection,(0,384))    #Affiche la fenêtre du bas, celle où l'on choisit notre action pour le tour
    window.blit(spr_hpBar,(220,30))    #Affiche le rectangle gris en fond de barre de vie
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))    #Dessine le rectangle rouge de la barre de vie en fonction de nos hps, simple proportionnalitée
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(420,40))    #Ecrit en blanc nos hps dans la barre de vie
    drawEnnemy()    #Fonction qui dessine tous les ennemis, à admirer tout à l'heure ;P
    #Ce if affiche quelque chose de différent suivant si notre compétence spéciale est prête ou pas
    if personnageFunctions.weapon.cooldown == 0 :
        window.blit(font.render("Compétence prête !",True,(150,150,150)),(382,460))
    else : 
        window.blit(font.render("Recharge :" + str(personnageFunctions.weapon.cooldown) + "/" + str(personnageFunctions.weapon.tempsCd),True,(150,150,150)),(382,460))
    window.blit(font.render("Potions :" + str(personnageFunctions.backpack.potion) + "/5",True,(150,150,150)),(750,460))    #Affiche le nombre de potions
    window.blit(spr_pointeurPerso,(80+ennemyCursor*186,96))    #Affiche le curseur jaune pour sélectionner les ennemis
  
    
#Cette fonction sert à dessiner toute la fenêtre graphique, avec le curseur de sélection de notre action de début de tour
#Elle est utilisée lorsque l'on choisit son action de début de tour      
def drawCursor(cursor) :
    
    global window
    
    #Je ne redessine pas tout ici car le curseur est au dessus du texte de sélection
    #Il suffit donc de redessiner le cadre de texte afin de rafraîchir la position du curseur
    
    window.blit(spr_selection,(0,384))
    if personnageFunctions.weapon.cooldown == 0 :
        window.blit(font.render("Compétence prête !",True,(150,150,150)),(382,460))
    else : 
        window.blit(font.render("Recharge :" + str(personnageFunctions.weapon.cooldown) + "/" + str(personnageFunctions.weapon.tempsCd),True,(150,150,150)),(382,460))
    window.blit(font.render("Potions :" + str(personnageFunctions.backpack.potion) + "/5",True,(150,150,150)),(750,460))
    
    #Dessine le curseur suivant son emplacement
    if cursor == 1 :
        window.blit(spr_pointeur,(97,435))
    if cursor == 2 :
        window.blit(spr_pointeur,(357,435))
    if cursor == 3:
        window.blit(spr_pointeur,(718,435))


#Cette fonction permet de dessiner tous les ennemis, en lisant la listEnnemy qui contient tous les ennemis en vie (précisions dans la classe ennemy)
#Utile pour abréger le texte lorsqu'il faut redessiner tout l'écran
def drawEnnemy() :
    
    global window
    
    for pos,mechant in enumerate(ennemy.listEnnemy) :    #Le for permet de lire toute la liste
        if mechant != 0 :    #Si il n'y a pas d'ennemi, l'emplacement de liste vaut 0; ainsi un ennemi sera tout ce qui est différent de 0
            
            #Suivant chaque ennemi, la position n'est pas la même puisque le dessin de chaque ennemi ne fait pas la même taille.
            #L'emplacement est proportionnel à pos, soit la position dans la liste de l'ennemi et donc son emplacement sur l'écran
            
            if mechant.name == "Gobelin" :
                
                window.blit(spr_gobelin,(pos*186,128))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpGobelin),True,(150,150,150)),(61+pos*186,290))
                    
            if mechant.name == "Chauve-souris" :
                
                window.blit(spr_bat,(13+pos*186,118))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpBat),True,(150,150,150)),(61+pos*186,265))
                    
            if mechant.name == "Comte Vladimir" :
                
                window.blit(spr_vampire,(30+pos*186,135))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpVladimir),True,(150,150,150)),(55+186*pos,350))                
            
            if mechant.name == "Araignee" : 
                                
                window.blit(spr_spider,(18+pos*186,100))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpSpider),True,(150,150,150)),(50+pos*186,270))
            
            if mechant.name == "Sorciere"  : 
            
                window.blit(spr_witch,(20+pos*186,140))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpWitch),True,(150,150,150)),(35+pos*186,323))
                
            if mechant.name == "Ogre" :
                
                window.blit(spr_ogre,(5+pos*186,140))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpOgre),True,(150,150,150)),(35+pos*186,350))    #Steak.
                
            if mechant.name == "Msmoke" or mechant.name == "Msmoke2"  or mechant.name == "Msmoke3" or mechant.name == "Msmoke4" : 
                
                window.blit(spr_Msmoke,(-10+pos*186,110))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpMsmoke),True,(150,150,150)),(40+pos*186,357))
                
            if mechant.name == "Msmoke_vladimir" :
                
                window.blit(spr_vampire,(30+pos*186,135))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpMsmoke),True,(150,150,150)),(55+186*pos,350))
                
            if mechant.name == "Msmoke_sorciere" :
                
                window.blit(spr_witch,(20+pos*186,140))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpMsmoke),True,(150,150,150)),(35+pos*186,323))
                
            if mechant.name == "Msmoke_ogre" :
                
                window.blit(spr_ogre,(5+pos*186,140))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpMsmoke),True,(150,150,150)),(35+pos*186,350))
                
            if mechant.name == "Minotaure" :
                
                window.blit(spr_minotaure,(-17+pos*186,100))
                window.blit(font.render("Hp : " + str(mechant.hp) + "/" + str(hpMinotaure),True,(150,150,150)),(40+pos*186,357))

 
"""
Cette fonction sert à initialiser la fenêtre graphique de pygame.
J'importe tous mes sprites et je les assignes à une variable str_, afin de ne pas se perdre.
"""    
def windowInitialisation(personnage) :
    
    global personnageFuctions

    personnageFunctions = personnage
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(350,40))
          
    drawEnnemy()

#Cette fonction permet de choisir notre action lors du début du combat
def askAction() :
    
    loop = True    
    cursor = 1    #Cursor est l'emplacement actuel du curseur entre les 3 actions, et est return lorsque on sélectionne
    
    global window   
    
    #Dessin classique de la fenêtre
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    if personnageFunctions.weapon.cooldown == 0 :
        window.blit(font.render("Compétence prête !",True,(150,150,150)),(382,460))
    else : 
        window.blit(font.render("Recharge :" + str(personnageFunctions.weapon.cooldown) + "/" + str(personnageFunctions.weapon.tempsCd),True,(150,150,150)),(382,460))
    window.blit(font.render("Potions :" + str(personnageFunctions.backpack.potion) + "/5",True,(150,150,150)),(750,460))
    
    while loop :    #Tant que le joueur ne valide pas son choix, on reste dans une boucle
        
        for event in pygame.event.get() :    #boucle pygame, ou l'on interagit avec l'interface graphique
            pygame.display.flip()    #Permet de rafraichir le visuel de la fenêtre
            
            if event.type == pygame.QUIT :   #Cette partie est dans toutes les boucles pygame, elle permet de quitter si l'on appuie sr la croix
                pygame.quit()
                exit()
            
            
            if event.type == pygame.KEYDOWN :      #Si le joueur appuie sur une touche
                if event.key == pygame.K_LEFT :     #Si cette touche est la gauche,
                    if cursor > 1 :                 #Et que le curseur n'est pas déjà à sa position la plus à gauche
                        cursor -= 1                  #On déplace le curseur et on le dessine
                        drawCursor(cursor)
                        pygame.display.flip()
                
                if event.key == pygame.K_RIGHT :     #De même pour la touche de droite
                    if cursor < 3 :
                        cursor += 1
                        drawCursor(cursor)
                        pygame.display.flip()
                
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or event.key == pygame.K_SPACE :    #Finalement, si l'on appuie sur entrée ou espace, on valide notre choix
                    if personnageFunctions.backpack.potion == 0 and cursor == 3:     #Si le joueur n'a plus de potions, on ne valide pas son choix de potions et la boucle reprend
                        continue
                    if personnageFunctions.weapon.cooldown != 0 and cursor == 2:      #De même si la compétence n'est pas rechargée
                        continue
                    loop = False    #On sort de la boucle : ce booléen passe à false
                    return cursor     #On renvoie la valeur du curseur quand le joueur a validé son choix


#Permet de redessiner tout l'écran sans aboir besoin du paramètre personnage, mais avec son substitut personnageFunctions, qui est régulièrement copié sur le personnage
def redrawBoardNoHP() :
    
    global window
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(420,40))
    if personnageFunctions.weapon.cooldown == 0 :
        window.blit(font.render("Compétence prête !",True,(150,150,150)),(382,460))
    else : 
        window.blit(font.render("Recharge :" + str(personnageFunctions.weapon.cooldown) + "/" + str(personnageFunctions.weapon.tempsCd),True,(150,150,150)),(382,460))
    window.blit(font.render("Potions :" + str(personnageFunctions.backpack.potion) + "/5",True,(150,150,150)),(750,460))
    
    drawEnnemy()
    
    pygame.display.flip()
     
    
#Ici, on redessine l'écran mais avec le paramètre personnage. On actualise aussi personnageFunctions
def redrawBoard(personnage) :
    
    window = f.window
    global personnageFunctions
    
    personnageFunctions = personnage
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(420,40))
    if personnage.weapon.cooldown == 0 :
        window.blit(font.render("Compétence prête !",True,(150,150,150)),(382,460))
    else : 
        window.blit(font.render("Recharge :" + str(personnageFunctions.weapon.cooldown) + "/" + str(personnageFunctions.weapon.tempsCd),True,(150,150,150)),(382,460))
    window.blit(font.render("Potions :" + str(personnageFunctions.backpack.potion) + "/5",True,(150,150,150)),(750,460))
    
    drawEnnemy()
    
    pygame.display.flip()


#Permet de choisir quel ennemi l'on va attaquer
def askTarget(personnage) :
    
    loop = True
    
    #Cette partie permet de potisionner le curseur sur le premier ennemi, celui le plus à gauche
    for x in range (0,5) :
        if ennemy.listEnnemy[x] != 0 :
            cursor = x
            break
    drawEnnemyCursor(cursor)
    
    while loop :    #Tant que le joueur n'a pas validé son choix, on boucle
        
        for event in pygame.event.get() :
            pygame.display.flip()
            
            if event.type == pygame.QUIT :   #Permet de quitter si l'on clique sur la croix
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN :    #si le joueur appuie sur une touche
                
                if event.key == pygame.K_LEFT :    #Si il appuie sur la touche de gauche
                    
                    change = True    #Change permet de ne se déplacer que d'une fois à chaque fois que l'on appuie sur la fleche
                    
                    for x in [4,3,2,1,0] :     #On parcourt les possibilitées de position des ennemis dans l'ordre inverse
                        if ennemy.listEnnemy[x] != 0 and change and x < cursor :   #Si l'on trouve un ennemi, et que l'on a pas encore changé de position, et que cette ennemi est plus à gauche que l'emplacement actuel de notre curseur
                            cursor = x    #On déplace le curseur
                            change = False    #On l'empeche de changer de valeur à nouveau
                            drawEnnemyCursor(cursor)    #On redessine le curseur
                            pygame.display.flip()    #Et on actualise la fenêtre graphique
                        
                if event.key == pygame.K_RIGHT :    #Idem pour la touche de droite
                    change = True
                    for x in [0,1,2,3,4] :
                        if ennemy.listEnnemy[x] != 0 and change and x > cursor :
                            cursor = x
                            change = False
                            drawEnnemyCursor(cursor)
                            pygame.display.flip()
                    
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN or event.key == pygame.K_SPACE :   #Quand le joueur valide son choix
                    loop = False    #On arrête la boucle
                    return cursor    #On renvoie la valeur du curseur à l'emplacement où le joueur a validé
        
#Permet de faire faire à chaque ennemi son action
def mobAction(personnage) : 
    
    for mechant in ennemy.listEnnemy :    #Pour tous les objets dans la liste ennemi
            if mechant != 0 :    #Si l'objet est bien un ennemi et pas un 0
                action(personnage,mechant)
                if not personnage.life :
                    break

#Permet aux attaques de s'effectuer avec des QTE pour les éviter.
def attack(personnage,ennemy):
    
    global window
    global spr_fleche
    
    """
    Suivant la position de l'ennemi, il n'aura pas les mêmes touches pour attaquer
    Ainsi, à chaque position, sont associées 4 touches
    Elles sont sélectionnées aléatoirement grâce à un simple randint
    """
        
    if ennemy.position == 0 :    
        
        randomNumber = randint(0,3)
        if randomNumber == 0 :    #Pour chaque possibilitée aléatoire :
            qteKey = pygame.K_q    #On assigne la touche sur laquelle on devra appuyer pour pygame (ici, la touche q sur un clavier qwerty)
            spr_qte = spr_A        #On assigne le sprite qui s'affichera à l'écran (ici, A car q correspond a A sur un clavier azerty)
        if randomNumber == 1 :    #On fait de même pour tout le reste
            qteKey = pygame.K_w
            spr_qte = spr_Z
        if randomNumber == 2 :
            qteKey = pygame.K_e
            spr_qte = spr_E
        if randomNumber == 3 :
            qteKey = pygame.K_r
            spr_qte = spr_R
    
    if ennemy.position == 1 :
        
        randomNumber = randint(0,3)
        if randomNumber == 0 :
            qteKey = pygame.K_a
            spr_qte = spr_Q
        if randomNumber == 1 :
            qteKey = pygame.K_s
            spr_qte = spr_S
        if randomNumber == 2 :
            qteKey = pygame.K_d
            spr_qte = spr_D
        if randomNumber == 3 :
            qteKey = pygame.K_f
            spr_qte = spr_F
        
    if ennemy.position == 2 :
        #Pour l'ennemi central, on joue avec les fleches.
        randomNumber = randint(0,3)
        if randomNumber == 0 :
            qteKey = pygame.K_DOWN
        if randomNumber == 1 :
            qteKey = pygame.K_RIGHT
        if randomNumber == 2 :
            qteKey = pygame.K_UP
        if randomNumber == 3:
            qteKey = pygame.K_LEFT
        #Je n'ai qu'un seul sprite de fleche que je fais tourner suivant où l'on doit appuyer
        spr_qte = pygame.transform.rotate(spr_fleche,90*randomNumber) 
        
    if ennemy.position == 3 :
       
        randomNumber = randint(0,3)
        if randomNumber == 0 :
            qteKey = pygame.K_z
            spr_qte = spr_W
        if randomNumber == 1 :
            qteKey = pygame.K_x
            spr_qte = spr_X
        if randomNumber == 2 :
            qteKey = pygame.K_c
            spr_qte = spr_C
        if randomNumber == 3 :
            qteKey = pygame.K_v
            spr_qte = spr_V
            
    if ennemy.position == 4 :
        #Le dernier ennemi est le plus faible, et n'a que deux touches sur lesquelles appuyer
        randomNumber = randint(0,1)
        if randomNumber == 0 :
            qteKey = pygame.K_b
            spr_qte = spr_B
        if randomNumber == 1 :
            qteKey = pygame.K_n
            spr_qte = spr_N
            
        
    window.blit(spr_qte,(63+ennemy.position*186,180))    #On dessine le qte à l'emplacement de l'ennemi 
    pygame.display.flip()  
             
    loop = True
    timer = 1
    damages = True
        
    pygame.time.set_timer(timer+1,2000)    #On met un évenement timer qui s'activera aux bout de 2000 ms, Cela permet de faire un QTE
        
    while loop :
            
        for event in pygame.event.get() :
                
            pygame.display.flip()
                
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN :   #Si l'on appuie sur une touche 
                if event.key == qteKey :    #Et que c'était celle attendu
                    loop = False    #On peut sortir de la boucle
                    damages = False     #On ne peut plus se prendre de dégâts
                
            if event.type == timer+1 :    #Quand l'évenement se déclenche, le temps est donc écoulé
                redrawBoardNoHP()
                pygame.display.flip()
                if damages :     #Si l'on a pas appuyé sur la touche, on se prend des dégâts
                    ennemy.dealDamage(personnage)    #On appelle la méthode faire des dégâts de l'ennemi
                loop = False    #On arrête la boucle
                break
          
#Cette fonction est utilisée pour le boss final.
#Elle est sensiblement semblable à celle du dessus, ormis que ici, le choix est entre toutes les touches 
def attackFinal(personnage,ennemy):
    
    global window
    global spr_fleche
    
    """
    Suivant la position de l'ennemi, il n'aura pas les mêmes touches pour attaquer
    Ainsi, à chaque position, sont associées 4 touches
    Elles sont sélectionnées aléatoirement grâce à un simple randint
    """
        
    randomNumber = randint(0,17)
    
    if randomNumber == 0 :    
        qteKey = pygame.K_q    
        spr_qte = spr_A        
    if randomNumber == 1 :    
        qteKey = pygame.K_w
        spr_qte = spr_Z
    if randomNumber == 2 :
        qteKey = pygame.K_e
        spr_qte = spr_E
    if randomNumber == 3 :
        qteKey = pygame.K_r
        spr_qte = spr_R
    if randomNumber == 4 :
        qteKey = pygame.K_a
        spr_qte = spr_Q
    if randomNumber == 5 :
        qteKey = pygame.K_s
        spr_qte = spr_S
    if randomNumber == 6 :
        qteKey = pygame.K_d
        spr_qte = spr_D
    if randomNumber == 7 :
        qteKey = pygame.K_f
        spr_qte = spr_F
    if randomNumber == 8 :
        qteKey = pygame.K_z
        spr_qte = spr_W
    if randomNumber == 9 :
        qteKey = pygame.K_x
        spr_qte = spr_X
    if randomNumber == 10 :
        qteKey = pygame.K_c
        spr_qte = spr_C
    if randomNumber == 11 :
        qteKey = pygame.K_v
        spr_qte = spr_V
    if randomNumber == 12 :
        qteKey = pygame.K_b
        spr_qte = spr_B
    if randomNumber == 13 :
        qteKey = pygame.K_n
        spr_qte = spr_N
    if randomNumber == 14 :
        qteKey = pygame.K_DOWN
        spr_qte = pygame.transform.rotate(spr_fleche,0)
    if randomNumber == 15 :
        qteKey = pygame.K_RIGHT
        spr_qte = pygame.transform.rotate(spr_fleche,90)
    if randomNumber == 16:
        qteKey = pygame.K_UP
        spr_qte = pygame.transform.rotate(spr_fleche,180)
    if randomNumber == 17:
        qteKey = pygame.K_LEFT
        spr_qte = pygame.transform.rotate(spr_fleche,270)
                
    
        
    window.blit(spr_qte,(63+ennemy.position*186,180))    #On dessine le qte à l'emplacement de l'ennemi 
    pygame.display.flip()  
             
    loop = True
    timerFinal = 1
    damages = True
        
    pygame.time.set_timer(timerFinal+1,2000)    #On met un évenement timer qui s'activera aux bout de 2000 ms, Cela permet de faire un QTE
        
    while loop :
            
        for event in pygame.event.get() :
                
            pygame.display.flip()
                
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN :   #Si l'on appuie sur une touche 
                if event.key == qteKey :    #Et que c'était celle attendu
                    loop = False    #On peut sortir de la boucle
                    damages = False     #On ne peut plus se prendre de dégâts
                
            if event.type == timerFinal+1 :    #Quand l'évenement se déclenche, le temps est donc écoulé
                redrawBoardNoHP()
                pygame.display.flip()
                if damages :     #Si l'on a pas appuyé sur la touche, on se prend des dégâts
                    ennemy.dealDamage(personnage)    #On appelle la méthode faire des dégâts de l'ennemi
                loop = False    #On arrête la boucle
                break               
        
#Permet de faire des actions différentes selon les ennemis
def action(personnage,ennemy) :
    
    if ennemy.apparition:    #Cette attribut permet de vérifier que le monstre n'a pas été invoqué ce tour ci
        
        redrawBoard(personnage)
        pygame.display.flip()
        
        if ennemy.name == "Gobelin"  or ennemy.name == "Chauve-souris" or ennemy.name == "Araignee" :    #Si l'ennemi est un de ceux la :
                attack(personnage,ennemy)    #Il attaquera simplement tous les tours
    
        if ennemy.name == "Comte Vladimir" or ennemy.name == "Msmoke_vladimir" :    #Si l'ennemi est le Comte Vladimir
        
            if len([i for i in ennemy.listEnnemy if i != 0]) < 3 and randint(1,10) < 5 :    #Si il y a moins de trois ennemis sur le plateau, alors avec une probabilitée de 0.4, on invoque
                
                window.blit(font.render("INVOCATION !",True,(255,50,50)),(420,100))    #On écrit que Vladimir invoque des chauves-souris
                pygame.display.flip()    #On actualise pour que cela se voit
                time.sleep(1.2)     #On attend pour laisser voir l'information
                
                count = 0
                for pos,i in enumerate(ennemy.listEnnemy):    #Dans la liste d'ennemi
                    if i == 0 :     #Si il n'y a pas d'ennemi à cette emplacement
                        ennemy.summonEnnemy(pos)    #On appelle la méthoe summon à cette position
                        count += 1    #On rajoute 1 au compteur
                    if count == 2:   #Quand on a invoqué deux ennemis, la boucle cesse
                        break
                
            else :   #Sinon, Vladimir attaque 
                attack(personnage,ennemy)          
         
            
        if ennemy.name == "Sorciere" or ennemy.name == "Msmoke_sorciere" :
            
            if len([i for i in ennemy.listEnnemy if i != 0 ]) < 2 :   #On invoque forcément 3 ennemis si il n'y a que la sorcière sur le plateau
                
                window.blit(font.render("INVOCATION !",True,(255,50,50)),(420,100))
                pygame.display.flip()
                time.sleep(1.2)
                
                count = 0
                for pos,i in enumerate(ennemy.listEnnemy) :
                    if i == 0 :
                        ennemy.summonEnnemy(pos)
                        count += 1
                    if count == 3 :
                        break
                    
            elif len([i for i in ennemy.listEnnemy if i != 0]) < 4 :  #On invoque forcément 2 ennemis si il n'y a que 3 ennemis ou moins sur le plateau
                
                window.blit(font.render("INVOCATION !",True,(255,50,50)),(420,100))
                pygame.display.flip()
                time.sleep(1.2)
                
                count = 0
                for pos,i in enumerate(ennemy.listEnnemy):
                    if i == 0 :
                        ennemy.summonEnnemy(pos)
                        count += 1
                    if count == 2 :
                        break             
                     
            elif len([i for i in ennemy.listEnnemy if i != 0]) < 5 :    #On invoque forcément un ennemi si il n'en manque qu'un sur le plateau
                 
                 window.blit(font.render("INVOCATION !",True,(255,50,50)),(420,100))
                 pygame.display.flip()
                 time.sleep(1.2)
                 
                 count = 0
                 for pos,i in enumerate(ennemy.listEnnemy):
                     if i == 0 :
                         ennemy.summonEnnemy(pos)
                         count += 1
                     if count == 1:
                         break
                     
            else :    #Sinon, la sorciere attaque
                attack(personnage,ennemy)
                
        if ennemy.name == "Ogre" or ennemy.name == "Msmoke_ogre" :
            
            if ennemy.count == 0 : #Tous les deux tours, l'ogre attaque 3 fois dans son tour
                ennemy.count = 2
                attack(personnage,ennemy)
                redrawBoard(personnage)
                time.sleep(0.2)
                attack(personnage,ennemy)
                redrawBoard(personnage)
                time.sleep(0.2)
                attack(personnage,ennemy)
            else :
                if len([i for i in ennemy.listEnnemy if i != 0 ]) < 3 :   #Sinon il invoque 1 gobelin pour sûr si il n'y a que 2 ennemis ou moins sur le tableau
                
                    window.blit(font.render("INVOCATION !",True,(255,50,50)),(420,100))
                    pygame.display.flip()
                    time.sleep(1.2)
                
                    count = 0
                    for pos,i in enumerate(ennemy.listEnnemy) :
                        if i == 0 :
                            ennemy.summonEnnemy(pos)
                            count += 1
                        if count == 1 :
                                break
                            
                else : #Sinon, il attaque simplement une fois
                    
                    attack(personnage,ennemy)
        
        if ennemy.name == "Minotaure" :   #On attaque l'ennemi 5 fois d'affilées
            
            for x in range (0,5) : 
                redrawBoard(personnage)
                time.sleep(0.2)
                attackFinal(personnage,ennemy)
        
        if ennemy.name == "Msmoke" :  #Msmoke ne peut pas prendre de dégats, il esquivera, se transformera et changera en Msmoke_vladimir
            
            window.blit(font.render("ATTAQUE ESQUIVE...",True,(50,50,255)),(380,100))
            pygame.display.flip()
            time.sleep(2)
            
            redrawBoardNoHP()
            
            window.blit(font.render("TRANSFORMATION !",True,(255,50,50)),(380,100))
            pygame.display.flip()
            time.sleep(2)
            
            ennemy.name = "Msmoke_vladimir"
            ennemy.summon = "Bat"
            
        if ennemy.name == "Msmoke2" :  #De même, en se transformant en Msmoke_sorciere
            
            if len([i for i in ennemy.listEnnemy if i != 0 ]) == 1 :
                window.blit(font.render("TRANSFORMATION !",True,(255,50,50)),(380,100))
                pygame.display.flip()
                time.sleep(2)
            
                ennemy.name = "Msmoke_sorciere"
                ennemy.summon = summonWitch
                
        if ennemy.name == "Msmoke3" :  #Idem, en se transformant en Msmoke_ogre
            
            if len([i for i in ennemy.listEnnemy if i != 0 ]) == 1 :
                window.blit(font.render("TRANSFORMATION !",True,(255,50,50)),(380,100))
                pygame.display.flip()
                time.sleep(2)
            
                ennemy.name = "Msmoke_ogre"
                ennemy.summon = summonOgre
         
        if ennemy.name == "Msmoke4" :  #De même, en se transformant en minotaure
            
            if len([i for i in ennemy.listEnnemy if i != 0 ]) == 1 :
                window.blit(font.render("TRANSFORMATION !",True,(255,50,50)),(380,100))
                pygame.display.flip()
                time.sleep(2)
            
                ennemy.name = "Minotaure"
                ennemy.damage = damageMinotaure
                ennemy.hp = hpMinotaure
                
        
                
            
        
def victory():    #Affiche un écran de victoire lorsque le combat est gagné
    spr_victoryScreen = pygame.image.load("Sprites/victory.jpg")
    window.fill((0,0,0))
    window.blit(spr_victoryScreen,(8,0))
    pygame.display.flip()
    loop = True
    
    
def defeat() :    #Affiche un écran de défaite lorsque le combat est perdu
    spr_defeatScreen = pygame.image.load("Sprites/defeat.jpg")
    window.fill((0,0,0))
    window.blit(spr_defeatScreen,(123,0))
    pygame.display.flip()
    loop = True
    menuPrincipal()
                    
                
#Finalement, toutes ces fonctions servent à invoquer plus facilement un ennemi en marquant simplement son nom.               
def gobelin(position) :
    
    return ennemy(position,name = nameGobelin,hp = hpGobelin,damage = damageGobelin,summon = summonGobelin, count = countGobelin)

def bat(position) :
    
    return ennemy(position,name = nameBat,hp = hpBat,damage = damageBat,summon = summonBat, count = countBat)

def spider(position) :
    
    return ennemy(position,name = nameSpider,hp = hpSpider,damage = damageSpider,summon = summonSpider, count = countSpider)

def vladimir(position) :
    
    return ennemy(position,name = nameVladimir,hp = hpVladimir,damage = damageVladimir,summon = summonVladimir, count = countVladimir)

def witch(position) : 
    
    return ennemy(position,name = nameWitch,hp = hpWitch,damage = damageWitch,summon = summonWitch, count = countWitch)

def ogre(position) :
    
    return ennemy(position,name = nameOgre,hp = hpOgre,damage = damageOgre,summon = summonOgre, count = countOgre)

def Msmoke(position) :
    
    return ennemy(position,name = nameMsmoke,hp = hpMsmoke,damage = damageMsmoke,summon = summonMsmoke, count = countMsmoke)

def minotaure(position) :
    return ennemy(position,name = nameMinotaure,hp = hpMinotaure,damage = damageMinotaure,summon = summonMinotaure, count = countMinotaure)


