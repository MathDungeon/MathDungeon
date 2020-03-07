from character import *
import pygame

def drawEnnemyCursor(cursor) :
    
    global window
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    drawEnnemy()
    
    if cursor == 0 :
        window.blit(spr_pointeurPerso,(80,96))
    if cursor == 1 :
        window.blit(spr_pointeurPerso,(265,96))
    if cursor == 2 :
        window.blit(spr_pointeurPerso,(450,96))
    if cursor == 3 :
        window.blit(spr_pointeurPerso,(635,96))
    if cursor == 4 :
        window.blit(spr_pointeurPerso,(820,96))
        
        
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
                if pos == 0 :
                    window.blit(spr_gobelin,(0,128))
                if pos == 1 :
                    window.blit(spr_gobelin,(186,128))
                if pos == 2 :
                    window.blit(spr_gobelin,(364,128))
                if pos == 3 :
                    window.blit(spr_gobelin,(550,128))
                if pos == 4 :
                    window.blit(spr_gobelin,(736,128))
                    
            if mechant.name == "Chauve-souris" :
                if pos == 0 :
                    window.blit(spr_bat,(13,118))
                if pos == 1 :
                    window.blit(spr_bat,(199,118))
                if pos == 2 :
                    window.blit(spr_bat,(377,118))
                if pos == 3 :
                    window.blit(spr_bat,(563,118))
                if pos == 4 :
                    window.blit(spr_bat,(749,118))
                    
            if mechant.name == "Comte Vladimir" :
                if pos == 0 :
                    window.blit(spr_vampire,(30,135))
                if pos == 1 :
                    window.blit(spr_vampire,(216,135))
                if pos == 2 :
                    window.blit(spr_vampire,(394,135))
                if pos == 3 :
                    window.blit(spr_vampire,(580,135))
                if pos == 4 :
                    window.blit(spr_vampire,(766,135))
                

def windowInitialisation() :
    
    global window
    global spr_dungeon
    global spr_pointeur
    global spr_selection
    global spr_gobelin
    global spr_bat
    global spr_vampire
    global spr_pointeurPerso
    
    pygame.init()

    height = 512
    weight = 928

    #Création de la fenêtre
    window = pygame.display.set_mode((weight,height))
    
    spr_dungeon = pygame.image.load("backgroundDungeon.jpg")
    spr_selection = pygame.image.load("selectionScreen.png")
    spr_pointeur = pygame.image.load("pointeur.png")
    spr_gobelin = pygame.image.load("gobelin.png")
    spr_bat = pygame.image.load("bat.png")
    spr_vampire = pygame.image.load("vampire.png")
    spr_pointeurPerso = pygame.image.load("pointeurPerso.png")
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
       
    
    
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
                
                if event.key == pygame.K_RIGHT :
                    if cursor < 3 :
                        cursor += 1
                        drawCursor(cursor)
                
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN :
                    loop = False
                    return cursor                                       
        
        
def redrawBoard() :
    
    global window 
    
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(spr_pointeur,(97,435))
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
                        
                if event.key == pygame.K_RIGHT :
                    change = True
                    for x in [0,1,2,3,4] :
                        if ennemy.listEnnemy[x] != 0 and change and x > cursor :
                            cursor = x
                            change = False
                            drawEnnemyCursor(cursor)
                    
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
    