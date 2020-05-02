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

level1 = [[(10,9),(11,9),(12,7),(12,8),(12,9),(13,6),(13,7),(14,5),(14,6),(14,7),(14,8),(15,5),(15,7),(15,8),(16,6),(16,7),(17,6),{(9,9):"Boss",(15,9):"Shop"}],[(14,5),(16,5),(12,6),(13,6),(14,6),(15,6),(16,6),(13,7),(14,7),(15,7),(16,7),(17,7),(12,8),(13,8),(17,8),(18,8),{(17,9):"Boss",(12,6):"Shop"}]]
level2 = [[(11,8),(11,9),(12,6),(12,8),(13,6),(13,8),(13,9),(13,10),(14,4),(14,5),(14,6),(14,7),(14,8),(14,10),(15,4),(15,6),(15,7),(16,7),(17,7),(17,8),{(10,8):"Boss",(12,5):"Shop"}],[(11,8),(11,9),(12,6),(12,8),(13,6),(13,8),(13,9),(13,10),(14,4),(14,5),(14,6),(14,7),(14,8),(14,10),(15,4),(15,6),(15,7),(16,7),(17,7),(17,8),{(10,8):"Boss",(12,5):"Shop"}]]
levels = [level1,level2]
#temp = [i for j in mape for i in j if i]