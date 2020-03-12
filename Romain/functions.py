from character import *
import pygame

def drawEnnemyCursor(cursor) :
    
    global window
    window.blit(spr_dungeon,(0,0))
    window.blit(spr_selection,(0,384))
    window.blit(font.render("Hp : " + str(personnageFunctions.hp) + "/100",True,(255,255,255)),(30,30))
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
                hpDisplay = "Hp : " + str(mechant.hp) + "/30"
                hps = font.render(hpDisplay,True,(150,150,150))
                if pos == 0 :
                    window.blit(spr_gobelin,(0,128))
                    window.blit(hps,(61,290))
                if pos == 1 :
                    window.blit(spr_gobelin,(186,128))
                    window.blit(hps,(247,290))
                if pos == 2 :
                    window.blit(spr_gobelin,(372,128))
                    window.blit(hps,(433,290))
                if pos == 3 :
                    window.blit(spr_gobelin,(558,128))
                    window.blit(hps,(619,290))
                if pos == 4 :
                    window.blit(spr_gobelin,(744,128))
                    window.blit(hps,(805,290))
                    
            if mechant.name == "Chauve-souris" :
                hpDisplay = "Hp : " + str(mechant.hp) + "/10"
                hps = font.render(hpDisplay,True,(150,150,150))
                if pos == 0 :
                    window.blit(spr_bat,(13,118))
                    window.blit(hps,(61,265))
                if pos == 1 :
                    window.blit(spr_bat,(199,118))
                    window.blit(hps,(247,265))
                if pos == 2 :
                    window.blit(spr_bat,(385,118))
                    window.blit(hps,(433,265))
                if pos == 3 :
                    window.blit(spr_bat,(571,118))
                    window.blit(hps,(619,265))
                if pos == 4 :
                    window.blit(spr_bat,(757,118))
                    window.blit(hps,(805,265))
                    
            if mechant.name == "Comte Vladimir" :
                hpDisplay = "Hp : " + str(mechant.hp) + "/100"
                hps = font.render(hpDisplay,True,(150,150,150))
                if pos == 0 :
                    window.blit(spr_vampire,(30,135))
                    window.blit(hps,(55,350))
                if pos == 1 :
                    window.blit(spr_vampire,(216,135))
                    window.blit(hps,(241,350))
                if pos == 2 :
                    window.blit(spr_vampire,(402,135))
                    window.blit(hps,(427,350))
                if pos == 3 :
                    window.blit(spr_vampire,(588,135))
                    window.blit(hps,(613,350))
                if pos == 4 :
                    window.blit(spr_vampire,(774,135))
                    window.blit(hps,(799,350))
                

def windowInitialisation(personnage) :
    
    global window
    global spr_dungeon
    global spr_pointeur
    global spr_selection
    global spr_gobelin
    global spr_bat
    global spr_vampire
    global spr_pointeurPerso
    global font
    global personnageFuctions
    
    pygame.init()

    personnageFunctions = personnage

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
    