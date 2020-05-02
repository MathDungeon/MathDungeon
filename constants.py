"""
Code by Remi
"""

"""
Constants
"""

import pygame
from character import *

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

playerSprite1 = pygame.image.load("Sprites/player.png")
bossSprite = pygame.image.load("Sprites/boss.png")
shopSprite = pygame.image.load("Sprites/coin.png")
visibleTileSprite = pygame.image.load("Sprites/visibleTile.png")
notVisibleTileSprite = pygame.image.load("Sprites/notVisibleTile.png")
keyESprite = pygame.image.load("Sprites/keyE.png")
trapdoorSprite = pygame.image.load("Sprites/trapdoor.png")

#Font

font = pygame.font.SysFont('arial', 24)
        
#Map
        
mape = []
for i in range(0,16):
    mape.append([])
    for j in range(0,29):
        mape[i].append(None)

def mapf(coord):
	x,y = coord
	return mape[y][x]

#temp = [i for j in mape for i in j if i]