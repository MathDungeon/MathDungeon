"""
Code by Remi
"""

import pygame
import constants as const
import classes as clas
from sys import exit,platform

#Functions

"""
Vars
"""

#Coordinates
xPlayer = 14
yPlayer = 7

level = 1

"""
Classes
"""

class tile:
    """
    Define:
    Coordinates
    If tile has been visited yet
    What does the tile contains
    """
    
    def __init__(self,x,y,isVisible=False,content=None):
        
        self.x = x
        self.y = y
        self.isVisible = isVisible
        self.content = content
        self.tileDraw()
        const.mape[self.y][self.x] = self
    
    def tileDraw(self):
        global window
        if self.isVisible:
            window.blit(const.visibleTileSprite,((self.x*32),(self.y*32)))
        else:
            window.blit(const.notVisibleTileSprite,((self.x*32),(self.y*32)))

    def discover(self):
        self.isVisible = True

"""
Functions
"""

def varFraming(var,vmin,vmax):
    if var < vmin:
        return vmin
    elif var > vmax:
        return vmax
    else:
        return var
def gameInit():

    #Declare window object
    global window

    #Initialize pygame and window
    pygame.init()
    window = pygame.display.set_mode((const.weight, const.height))

def draw():

    global xPlayer
    global yPlayer
    #global tile

    #Clear BG
    window.fill(const.defaultBGColor)

    for line in const.mape:
        for tile in line:
            if tile:
                tile.tileDraw()

    playerDraw(xPlayer, yPlayer)

    #Update window
    pygame.display.flip()


def gameLoop():
    global xPlayer
    global yPlayer
    #Initialize gameQuit boolean that breaks the loop
    gameQuit = False
    while not gameQuit:
        movement = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                gameQuit = True
            if platform == 'linux':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z and const.mape[yPlayer-1][xPlayer]:
                    yPlayer -= 1
                    movement = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and const.mape[yPlayer+1][xPlayer]:
                    yPlayer += 1
                    movement = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q and const.mape[yPlayer][xPlayer-1]:
                    xPlayer -= 1
                    movement = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d and const.mape[yPlayer][xPlayer+1]:
                    xPlayer += 1
                    movement = True
            if platform == 'win32':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w and const.mape[yPlayer-1][xPlayer]:
                    yPlayer -= 1
                    movement = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s and const.mape[yPlayer+1][xPlayer]:
                    yPlayer += 1
                    movement = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a and const.mape[yPlayer][xPlayer-1]:
                    xPlayer -= 1
                    movement = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d and const.mape[yPlayer][xPlayer+1]:
                    xPlayer += 1
                    movement = True
        xPlayer = varFraming(xPlayer, 0, const.cWeight)
        yPlayer = varFraming(yPlayer, 0, const.cHeight)
        if movement == True and const.mape[yPlayer][xPlayer]:
            const.mape[yPlayer][xPlayer].discover()
        draw()
    pygame.quit()
    exit()

def playerDraw(x,y):
    #TODO convert into coordinates with pixels
    window.blit(const.playerSprite1, (32*x, 32*y))

def generateMap():
    tile(9,9)
    tile(10,9)
    tile(11,9)
    tile(12,7)
    tile(12,8)
    tile(12,9)
    tile(13,6)
    tile(13,7)
    tile(14,5)
    tile(14,6)
    tile(14,7,True)
    tile(14,8)
    tile(15,5)
    tile(15,7)
    tile(15,8)
    tile(15,9)
    tile(16,6)
    tile(16,7)
    tile(17,6)