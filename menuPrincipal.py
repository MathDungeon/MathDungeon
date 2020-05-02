"""
Code by Léo
"""
import pygame, sys                         #J'importe les modules et les fichiers dont j'ai besoin
from pygame.locals import *

"""
Ce ficher sert à créer le menu principal via lequel le joueur va accéder au jeu
"""

spr_curseur = pygame.image.load("Sprites/test_curseur_jaune.png") #J'importe les images dont j'ai besoin et je les associe à une variable

def menuPrincipal():
    pygame.init() #On initialise pygame

    window = pygame.display.set_mode((928,512)) #On crée la fenêtre de jeu

    BLACK=(0,0,0)                               #Je crée les variables que j'utiliserai plus tard
    MPcursor = 1
    
    font5 = pygame.font.SysFont('Courier', 27)  #Je crée les polices d'écritures dont j'ai besoin et les assigne à une variable
    font6 = pygame.font.SysFont('Courier', 70)

    window.fill(BLACK)                                                      #Je dessine le menu principal                 
    window.blit(spr_curseur,(403,265))
    window.blit(font6.render('MATH', False, (255,255,255)),(325,25))
    window.blit(font6.render('DUNGEON', False, (255,255,255)),(385,70))        
    window.blit(font5.render('JOUER', False, (255,255,255)),(425,265))
    window.blit(font5.render('QUITTER', False, (255,255,255)),(410,295))

    while True:
        for event in pygame.event.get() :  
            if event.type==QUIT :    #Cette boucle sert à quitter la fenêtre si le joueur clique sur la croix
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN :   #Cette boucle sert à détecter si une touche est pressée
                if event.key != pygame.K_RETURN and event.key != pygame.K_DOWN and event.key != pygame.K_UP : #Cette boucle sert à ce qu'il ne se passe rien si le joueur appuie sur une touche autre que celles qui sont utiles (en raison de certains bugs)
                    pass
                
                if event.key == pygame.K_DOWN :    #Ces deux boucles servent à modifier la valeur de la variable MPcursor si le joueur appuie sur les flèches du haut ou du bas
                    MPcursor += 1
                if event.key == pygame.K_UP :
                    MPcursor -= 1
                
                if MPcursor > 2 :    #Ces deux boucles servent à encadrer la variable MPcursor
                    MPcursor = 1
                if MPcursor < 1 :
                    MPcursor = 2
                
                if MPcursor == 1 :                                                         #Ces deux boucles servent à dessiner le curseur à des endroits différents en fonction de la valeur de la variable MPcursor
                    window.fill(BLACK)
                    window.blit(spr_curseur,(403,265))
                    window.blit(font6.render('MATH', False, (255,255,255)),(325,25))
                    window.blit(font6.render('DUNGEON', False, (255,255,255)),(385,70))
                    window.blit(font5.render('JOUER', False, (255,255,255)),(425,265))
                    window.blit(font5.render('QUITTER', False, (255,255,255)),(410,295))
                if MPcursor == 2 :
                    window.fill(BLACK)
                    window.blit(spr_curseur,(385,295))
                    window.blit(font6.render('MATH', False, (255,255,255)),(325,25))
                    window.blit(font6.render('DUNGEON', False, (255,255,255)),(385,70))
                    window.blit(font5.render('JOUER', False, (255,255,255)),(425,265))
                    window.blit(font5.render('QUITTER', False, (255,255,255)),(410,295))
                
                
                    
                if event.key == K_RETURN and MPcursor == 2 : #Cette boucle sert à quitter la fenêtre si le joueur sélectionne l'option "QUITTER"
                    pygame.quit()
                    sys.exit()
                
        pygame.display.update()    #Cette commande sert à actualiser la fenêtre de jeu

menuPrincipal()
