"""
Code by Remi
"""

import pygame
import constants as const
import character as ch
import random as rand
import mainRomain as rom1
from menuMarchand import *
from sys import exit,platform
from tile import tile

#Functions

"""
Vars
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

    global player
    player = ch.character()
    #Initialize pygame and window
    pygame.init()
    window = pygame.display.set_mode((const.weight, const.height))
    rand.seed()

    pygame.display.set_caption("MathDungeon")

def draw():
    #Clear BG
    window.fill(const.defaultBGColor)

    for line in const.mape:
        for t in line:
            if t:
                t.tileDraw()

    playerDraw(player.x, player.y)
    player.tile.interact()

    #Update window
    pygame.display.flip()


def gameLoop():
    #Initialize gameQuit boolean that breaks the loop
    gameQuit = False
    while not gameQuit:
        level = 1
        reset = False
        global generated
        global player
        r_down = False
        while not reset:
            reset = False
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    gameQuit = True
                    reset = True
                if platform == 'linux':
                    keys = {pygame.K_z:(player.y-1,player.x),pygame.K_s:(player.y+1,player.x),pygame.K_q:(player.y,player.x-1),pygame.K_d:(player.y,player.x+1)}
                elif platform == 'win32':
                    keys = {pygame.K_w:(player.y-1,player.x),pygame.K_s:(player.y+1,player.x),pygame.K_a:(player.y,player.x-1),pygame.K_d:(player.y,player.x+1)}
                for key,cont in keys.items():
                    y,x = cont
                    if event.type == pygame.KEYDOWN and event.key == key and const.mape[y][x]:
                        player.move(x,y)
                        player.tile.discover()
                        if player.tile.content == "Boss":
                            rom1.boss(level)
                            player.tile.content = "Defeated_Boss"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    clrMap()
                    level = 1
                    del player
                    player = ch.character()
                    reset = True

                if player.tile:
                    if player.tile.content:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                            if player.tile.content == "Defeated_Boss":
                                level += 1
                                player.move(14,7)
                                clrMap()
                                if level == 4:
                                    rom1.boss(level)
                            if player.tile.content == "Shop":
                                menuMarchand()
            if not (generated or level == 4):
                generateMap(level)
            draw()
    clrMap()
    pygame.quit()
    exit()

def clrMap():
    global generated
    for i in const.mape:
        for j in i:
            if j:
                j.clear()
    generated = False

def playerDraw(x,y):
    #TODO convert into coordinates with pixels
    window.blit(const.playerSprite1, (32*x, 32*y))

def generateMap(level):
    global generated
    tileNumber = (19, 24, 34,1)
    tile((player.x, player.y), True)
    tile((15,7))
    temp = [i for j in const.mape for i in j if i]
    while len(temp) < tileNumber[level-1]:
        rand.choice(temp).generate()
        temp = [i for j in const.mape for i in j if i]
    player.tile.discover()
    temp = [i for j in const.mape for i in j if i]
    temp = [i for i in temp if i.neighborsNb == 1]
    boss = rand.randrange(len(temp))
    temp.pop(boss).content = "Boss"
    shop = rand.randrange(len(temp))
    temp.pop(shop).content = "Shop"
    generated = True