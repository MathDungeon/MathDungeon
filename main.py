import pygame
import constants as const

def gameLoop():

	gameQuit = False
	while not gameQuit:

		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				gameQuit = True

		draw()
	pygame.quit()
	exit()

def gameInit():

	global window

	pygame.init()
	window = pygame.display.set_mode((const.weight, const.height))

def draw():

	window.fill(const.colorGrey)

gameInit()
gameLoop()