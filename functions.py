"""
Code by Remi
"""

import pygame
import constants as const
from sys import exit,platform

#Functions

"""
Vars
"""

#Coordinates
xPlayer = 0
yPlayer = 0

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
    
    def __init__(self,x,y,content=None):
        
        self.x = x
        self.y = y
        self.isVisible = False
        self.content = content
        self.tileDraw()
        const.mape[self.y][self.x] = self
    
    def tileDraw(self):
        global window
        window.blit(const.tileSprite,(self.x,self.y))

    def discover(self):
    	self.isVisible = True

"""
Functions
"""

def varFraming(var ,min, max):
    if var < min:
        return min

    if var > max:
        return max

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

    #tiles = tile(0,0)

    xPlayer = varFraming(xPlayer, 0, const.weight-33)
    yPlayer = varFraming(yPlayer, 0, const.height-33)

    playerDraw(xPlayer, yPlayer)

    #Update window
    pygame.display.flip()


def gameLoop():
    global xPlayer
    global yPlayer
    #Initialize gameQuit boolean that breaks the loop
    gameQuit = False
    while not gameQuit:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                gameQuit = True
            if platform == 'linux':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    yPlayer -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    yPlayer += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    xPlayer -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    xPlayer += 1
            if platform == 'win32':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    yPlayer -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    yPlayer += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    xPlayer -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    xPlayer += 1

        draw()
    pygame.quit()
    exit()

def playerDraw(x,y):
    #TODO convert into coordinates with pixels
    print(x,y)
    #window.blit(const.playerSprite1, (32*x, 32*y))
    #print(x,",",y)