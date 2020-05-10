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
width = 928
cHeight = 15
cWidth = 28

#Colors

colorBlack = (0,0,0)
colorWhite = (255,255,255)
colorGrey = (100,100,100)

#Sprites

playerSprite1 = pygame.image.load("Sprites/player.png")
bossSprite = pygame.image.load("Sprites/boss.png")
shopSprite = pygame.image.load("Sprites/coin.png")
visibleTileSprite = pygame.image.load("Sprites/visibleTile.png")
notVisibleTileSprite = pygame.image.load("Sprites/notVisibleTile.png")
keyESprite = pygame.image.load("Sprites/keyE.png")
trapdoorSprite = pygame.image.load("Sprites/trapdoor.png")
spiderSprite = pygame.image.load("Sprites/spider.png")
blacksmithSprite = pygame.image.load("Sprites/anvil.png")

spr_dungeon = pygame.image.load("Sprites/backgroundDungeon.jpg")
spr_selection = pygame.image.load("Sprites/selectionScreen.png")
spr_pointeur = pygame.image.load("Sprites/pointeur.png")
spr_gobelin = pygame.image.load("Sprites/gobelin.png")
spr_bat = pygame.image.load("Sprites/bat.png")
spr_vampire = pygame.image.load("Sprites/vampire.png")
spr_spider = pygame.image.load("Sprites/araignee.png")
spr_witch = pygame.image.load("Sprites/sorciere.png")
spr_ogre = pygame.image.load("Sprites/ogre.png")
spr_Msmoke = pygame.image.load("Sprites/smokeMonster.png")
spr_minotaure = pygame.image.load("Sprites/minotaure.png")
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