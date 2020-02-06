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

global xPlayer
global yPlayer
xPlayer = 0
yPlayer = 0

"""
Functions
"""

def varFraming(var ,min, max):
	if var < min:
		var = min

	if var > max:
		var = max

def gameInit():

    #Declare window object
    global window

    #Initialize pygame and window
    pygame.init()
    window = pygame.display.set_mode((const.weight, const.height))

def draw():

	global xPlayer
	global yPlayer

	#Clear BG
	window.fill(const.defaultBGColor)

	varFraming(xPlayer, 0, const.weight-33)
	varFraming(yPlayer, 0, const.height-33)

	playerDraw(xPlayer, yPlayer)

    #Update window
    pygame.display.flip()


def gameLoop():
	
    #Initialize gameQuit boolean that breaks the loop
    gameQuit = False
    while not gameQuit:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                gameQuit = True
            if platform == 'linux':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                    const.yPlayer -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    const.yPlayer += 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    const.xPlayer -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    const.xPlayer += 1

        draw()
    pygame.quit()
    exit()

def playerDraw(x,y):
    #TODO convert into coordinates with pixels
    
    window.blit(const.playerSprite1, (x*32, y*32))
    #print(x,",",y)

#Classes
    
class tile:
    """
    Define:
    Coordinates
    If tile has been visited yet
    What does the tile contains
    """
    
    def __init__(self,x,y):
        
        self.x = x
        self.y = y
        self.isVisible = False
        self.tileDraw()
        mape[self.x][self.y] = self
    
    def tileDraw(self):
        window.blit(const.tileSprite,(self.x,self.y))
        
#Map
        
mape = [
       [0,0,0],
       [0,0,0],
       [0,0,0],
      ]