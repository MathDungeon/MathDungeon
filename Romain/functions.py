from character import *
from random import randint
import pygame

def drawEnnemyCursor(cursor) :
    
    global window
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(420,40))
    drawEnnemy()
    
    window.blit(spr_pointeurPerso,(80+cursor*186,96))        
        
def drawCursor(cursor) :
    
    global window
    window.blit(spr_selection,(0,384))
    
    if cursor == 1 :
        window.blit(spr_pointeur,(97,435))
    if cursor == 2 :
        window.blit(spr_pointeur,(357,435))
    if cursor == 3:
        window.blit(spr_pointeur,(718,435))

def drawEnnemy() :
    
    global window
    
    for pos,mechant in enumerate(ennemy.listEnnemy) :
        if mechant != 0 :
            
            if mechant.name == "Gobelin" :
                
                hpDisplay = "Hp : " + str(mechant.hp) + "/30"
                hps = font.render(hpDisplay,True,(150,150,150))
                
                window.blit(spr_gobelin,(pos*186,128))
                window.blit(hps,(61+pos*186,290))
                    
            if mechant.name == "Chauve-souris" :
                
                hpDisplay = "Hp : " + str(mechant.hp) + "/10"
                hps = font.render(hpDisplay,True,(150,150,150))
                
                window.blit(spr_bat,(13+pos*186,118))
                window.blit(hps,(61+pos*186,265))
                    
            if mechant.name == "Comte Vladimir" :
                
                hpDisplay = "Hp : " + str(mechant.hp) + "/100"
                hps = font.render(hpDisplay,True,(150,150,150))
                
                window.blit(spr_vampire,(30+pos*186,135))
                window.blit(hps,(55+186*pos,350))                

def windowInitialisation(personnage) :
    
    global window
    global spr_dungeon
    global spr_pointeur
    global spr_selection
    global spr_gobelin
    global spr_bat
    global spr_vampire
    global spr_pointeurPerso
    global spr_hpBar
    global spr_fleche
    
    global spr_A
    global spr_B
    global spr_C
    global spr_D
    global spr_E
    global spr_F
    global spr_G
    global spr_H
    global spr_I
    global spr_J
    global spr_K
    global spr_L
    global spr_M
    global spr_N
    global spr_O
    global spr_P
    global spr_Q
    global spr_R
    global spr_S
    global spr_T
    global spr_U
    global spr_V
    global spr_W
    global spr_X
    global spr_Y
    global spr_Z 
        
    global font
    global personnageFuctions
    
    pygame.init()

    personnageFunctions = personnage

    height = 512
    weight = 928

    #Création de la fenêtre
    window = pygame.display.set_mode((weight,height))
    
    spr_dungeon = pygame.image.load("Sprites/backgroundDungeon.jpg")
    spr_selection = pygame.image.load("Sprites/selectionScreen.png")
    spr_pointeur = pygame.image.load("Sprites/pointeur.png")
    spr_gobelin = pygame.image.load("Sprites/gobelin.png")
    spr_bat = pygame.image.load("Sprites/bat.png")
    spr_vampire = pygame.image.load("Sprites/vampire.png")
    spr_pointeurPerso = pygame.image.load("Sprites/pointeurPerso.png")
    spr_hpBar = pygame.image.load("Sprites/hpBar.png")
    spr_fleche = pygame.image.load("Sprites/fleche.png")
    
    spr_A = pygame.image.load("Sprites/Lettres/A.png")
    spr_B = pygame.image.load("Sprites/Lettres/B.png")
    spr_C = pygame.image.load("Sprites/Lettres/C.png")
    spr_D = pygame.image.load("Sprites/Lettres/D.png")
    spr_E = pygame.image.load("Sprites/Lettres/E.png")
    spr_F = pygame.image.load("Sprites/Lettres/F.png")
    spr_G = pygame.image.load("Sprites/Lettres/G.png")
    spr_H = pygame.image.load("Sprites/Lettres/H.png")
    spr_I = pygame.image.load("Sprites/Lettres/I.png")
    spr_J = pygame.image.load("Sprites/Lettres/J.png")
    spr_K = pygame.image.load("Sprites/Lettres/K.png")
    spr_L = pygame.image.load("Sprites/Lettres/L.png")
    spr_M = pygame.image.load("Sprites/Lettres/M.png")
    spr_N = pygame.image.load("Sprites/Lettres/N.png")
    spr_O = pygame.image.load("Sprites/Lettres/O.png")
    spr_P = pygame.image.load("Sprites/Lettres/P.png")
    spr_Q = pygame.image.load("Sprites/Lettres/Q.png")
    spr_R = pygame.image.load("Sprites/Lettres/R.png")
    spr_S = pygame.image.load("Sprites/Lettres/S.png")
    spr_T = pygame.image.load("Sprites/Lettres/T.png")
    spr_U = pygame.image.load("Sprites/Lettres/U.png")
    spr_V = pygame.image.load("Sprites/Lettres/V.png")
    spr_W = pygame.image.load("Sprites/Lettres/W.png")
    spr_X = pygame.image.load("Sprites/Lettres/X.png")
    spr_Y = pygame.image.load("Sprites/Lettres/Y.png")
    spr_Z = pygame.image.load("Sprites/Lettres/Z.png")
    
    font = pygame.font.SysFont('arial', 24)
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(350,40))
           
    
    drawEnnemy()
    
    pygame.display.set_caption("Window")                

def askAction() :
    
    loop = True
    cursor = 1
    
    global window   
    
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    
    while loop :
        
        for event in pygame.event.get() :
            pygame.display.flip()
            
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    if cursor > 1 :
                        cursor -= 1
                        drawCursor(cursor)
                        pygame.display.flip()
                
                if event.key == pygame.K_RIGHT :
                    if cursor < 3 :
                        cursor += 1
                        drawCursor(cursor)
                        pygame.display.flip()
                
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN :
                    loop = False
                    return cursor 

def redrawBoardNoHP() :
    
    global window
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(420,40))
    drawEnnemy()
     
def redrawBoard(personnage) :
    
    global window 
    global personnageFunctions
    
    personnageFunctions = personnage
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(420,40))
    drawEnnemy()

def askTarget(personnage) :
    
    loop = True
    
    for x in range (0,5) :
        if ennemy.listEnnemy[x] != 0 :
            cursor = x
            break
    drawEnnemyCursor(cursor)
    while loop :
        
        for event in pygame.event.get() :
            pygame.display.flip()
            
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    change = True
                    for x in [4,3,2,1,0] :
                        if ennemy.listEnnemy[x] != 0 and change and x < cursor :
                            cursor = x
                            change = False
                            drawEnnemyCursor(cursor)
                            pygame.display.flip()
                        
                if event.key == pygame.K_RIGHT :
                    change = True
                    for x in [0,1,2,3,4] :
                        if ennemy.listEnnemy[x] != 0 and change and x > cursor :
                            cursor = x
                            change = False
                            drawEnnemyCursor(cursor)
                            pygame.display.flip()
                    
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN :
                    loop = False
                    return cursor
        

def mobAction(personnage) : 
    
    for mechant in ennemy.listEnnemy :
            if mechant != 0 :
                action(personnage,mechant)
                if not personnage.life :
                    break

def attack(personnage,ennemy):
    
    global window
    global spr_fleche
    
    if ennemy.position == 0 :
        
        randomNumber = randint(0,3)
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
        
        randomNumber = randint(0,3)
        if randomNumber == 0 :
            qteKey = pygame.K_DOWN
        if randomNumber == 1 :
            qteKey = pygame.K_RIGHT
        if randomNumber == 2 :
            qteKey = pygame.K_UP
        if randomNumber == 3:
            qteKey = pygame.K_LEFT
        
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
        
        randomNumber = randint(0,1)
        if randomNumber == 0 :
            qteKey = pygame.K_b
            spr_qte = spr_B
        if randomNumber == 1 :
            qteKey = pygame.K_n
            spr_qte = spr_N
            
        
    window.blit(spr_qte,(63+ennemy.position*186,180))
    pygame.display.flip()  
             
    loop = True
    timer = 1
    damages = True
        
    pygame.time.set_timer(timer+1,2000)
        
    while loop :
            
        for event in pygame.event.get() :
                
            pygame.display.flip()
                
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN :
                if event.key == qteKey :
                    loop = False
                    damages = False
                
            if event.type == timer+1 :
                redrawBoardNoHP()
                pygame.display.flip()
                if damages :
                    ennemy.dealDamage(personnage)
                loop = False
                break
            
                
        

def action(personnage,ennemy) :
    
    if ennemy.apparition:
    
        if ennemy.name == "Gobelin" or ennemy.name == "Squelette" or ennemy.name == "Chauve-souris" :
                attack(personnage,ennemy)
        
        if ennemy.name == "Troll" :
                
            if ennemy.count == 0 :
                attack(personnage,ennemy)
                ennemy.count = 1
            else : 
                ennemy.count -= 1
    
        if ennemy.name == "Comte Vladimir" :
        
            if len([i for i in ennemy.listEnnemy if i != 0]) < 3 and randint(1,10) < 5 :
                count = 0
                for pos,i in enumerate(ennemy.listEnnemy):
                    if i == 0 :
                        ennemy.summonEnnemy(pos)
                        count += 1
                    if count == 2:
                        break
                
            else :
                attack(personnage,ennemy)
       
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
    