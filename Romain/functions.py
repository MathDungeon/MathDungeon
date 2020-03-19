from character import *
import pygame

def drawEnnemyCursor(cursor) :
    
    global window
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(30,30))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
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
    font = pygame.font.SysFont('arial', 24)
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(30,30))
           
    
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
        
        
def redrawBoard(personnage) :
    
    global window 
    global personnageFunctions
    
    personnageFunctions = personnage
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(30,30))
    window.blit(spr_hpBar,(220,30))
    pygame.draw.rect(window,(255,0,0),(243,33,int(personnageFunctions.hp*4.54),44))
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
    