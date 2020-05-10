"""
Code by Remi
"""

import pygame
import os
import constants as const
import character as ch
import random as rand
import mainRomain as rom1
from menuMarchand import *
from menuForgeron import *
from sys import platform
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
    window = pygame.display.set_mode((const.width, const.height))
    rand.seed()

def draw():

    global player

    #Clear BG
    window.blit(const.spr_dungeon,(0,0))

    for line in const.mape:
        for t in line:
            if t:
                t.tileDraw()

    text = const.font.render("Votre argent : {0}".format(player.gold), True, const.colorWhite)
    window.blit(text,(20,20))

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
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and (pygame.K_LALT or pygame.K_RALT)):
                    pygame.quit()
                    os._exit(1)
                if platform == 'linux':
                    keys = {pygame.K_UP:(player.y-1,player.x),pygame.K_DOWN:(player.y+1,player.x),pygame.K_LEFT:(player.y,player.x-1),pygame.K_RIGHT:(player.y,player.x+1)}
                elif platform == 'win32':
                    keys = {pygame.K_UP:(player.y-1,player.x),pygame.K_DOWN:(player.y+1,player.x),pygame.K_LEFT:(player.y,player.x-1),pygame.K_RIGHT:(player.y,player.x+1)}
                for key,cont in keys.items():
                    y,x = cont
                    if event.type == pygame.KEYDOWN and event.key == key and const.mape[y][x]:
                        player.move(x,y)
                        player.tile.discover()
                        if player.tile.content == "Boss":
                            rom1.boss(level)
                            player.tile.content = "Defeated_Boss"
                        if player.tile.content == "Mob":
                            rom1.mob(level)
                            player.tile.content = None
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
                                menuMarchand(player)
                            if player.tile.content == "Blacksmith":
                                menuForgeron(player)
            if not (generated or level == 4):
                generateMap(level)
            draw()
            if level == 4:
                gameQuit = True
                reset = True
    clrMap()

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
    enemyNumber = (4,5,7,0)
    loop = True
    while loop:
        try:
            tile((player.x, player.y), True, content = "Spawn")
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
            blacksmith = rand.randrange(len(temp))
            temp.pop(blacksmith).content = "Blacksmith"
        except ValueError:
            loop = True
            clrMap()
        else:
            loop = False
    generated = True
    temp = [i for j in const.mape for i in j if i]
    temp = [i for i in temp if i.content == None]
    for i in range(enemyNumber[level-1]):
        mob = rand.randrange(len(temp))
        temp.pop(mob).content = "Mob"