#Importation des bibliothèques nécessaires
import pygame

#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
window = pygame.display.set_mode((220,134))
fond = pygame.image.load("background.jpg")
window.blit(fond,(0,0))
pygame.display.set_caption("Window")

gameLoop = True

while gameLoop :
    
    pygame.display.flip()
    for event in pygame.event.get() :
        if (event.type == pygame.QUIT) :
            gameLoop = False
            
pygame.quit()