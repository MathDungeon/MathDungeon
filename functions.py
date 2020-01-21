"""
Code by Rémi
"""

import pygame
import constants as const

def gameInit():

	#Declare window object
	global window

	#Initialize pygame and window
	pygame.init()
	window = pygame.display.set_mode((const.weight, const.height))

def draw():

	#Clear BG
	window.fill(const.defaultBGColor)

	playerDraw(250,250)

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

		draw()
	pygame.quit()
	exit()

def playerDraw(xPlayer,yPlayer):
	#TODO convert into coordinates with pixels

	window.blit(const.playerSprite1, (xPlayer, yPlayer))
