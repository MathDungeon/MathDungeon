"""
Code by Remi
"""

"""
Constants
"""

import pygame

pygame.init()

#Window

height = 512
weight = 928
cHeight = 15
cWeight = 28

#Colors

colorBlack = (0,0,0)
colorWhite = (255,255,255)
colorGrey = (100,100,100)
defaultBGColor = (colorWhite)

#Sprites

playerSprite1 = pygame.image.load("Sprites/playerSprite1.png")
tileSprite = pygame.image.load("Sprites/tileSprite.png")

        
#Map
        
mape = [
       [None,None,None],
       [None,None,None],
       [None,None,None],
       ]