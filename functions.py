"""
Code by Remi
"""

import pygame
import constants as const
import character as ch
import random as rand
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
                            fightBoss = True
                            """
                            Combat de boss
                            """
                            player.tile.content = "Defeated_Boss"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    r_down = True
                    startTick = pygame.time.get_ticks()
                if event.type == pygame.KEYUP and event.key == pygame.K_r:
                    r_down = False
                if r_down:
                    if pygame.time.get_ticks() - startTick >= 500:
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
            if not generated:
                generateMap(level)
            draw()
    clrMap()
    print(const.mape)
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
    for i in rand.choice(const.levels[level-1]):
        if type(i) == tuple:
            tile(i,(i==(player.x,player.y)))
        elif type(i) == dict:
            for coord, cont in i.items():
                tile(coord, (coord==(player.x,player.y)), cont)
    player.tile.discover()
    generated = True