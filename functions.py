"""
Code by Rémi
"""

import pygame
import constants as const

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

	global xPlayer
	global yPlayer

	#Initialize gameQuit boolean that breaks the loop
	gameQuit = False
	while not gameQuit:

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
				gameQuit = True

			if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
				yPlayer -= 20
			if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				yPlayer += 20
			if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
				xPlayer -= 20
			if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
				xPlayer += 20
		draw()
	pygame.quit()
	exit()

def playerDraw(xPlayer,yPlayer):
	#TODO convert into coordinates with pixels

	window.blit(const.playerSprite1, (xPlayer, yPlayer))
