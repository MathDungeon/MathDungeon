# -*- coding: utf-8 -*-
"""
Code by Léo
"""
import pygame, sys                #J'importe les modules et les fichiers dont j'ai besoin
from pygame.locals import *
from ennemy import *
from functions import *
from romainFunctions import *
from constantFight import *
from character import *

"""
Ce ficher sert à créer le menu du marchand via lequel le joueur pourra acheter des objets
"""

spr_menu = pygame.image.load("Sprites/menu.png")                     #J'importe les images dont j'ai besoin et je les associe à une variable
spr_curseur = pygame.image.load("Sprites/test_curseur_jaune.png")
spr_coin = pygame.image.load("Sprites/coin2.png")

def menuMarchand(player):
    pygame.init()   #On initialise pygame

    window = pygame.display.set_mode((928,512)) #On crée la fenêtre de jeu

    WHITE = (255,255,255)           #Je crée les variables que j'utiliserai plus tard
    cursor = 0    #Cette variable va servir à stocker la position du curseur
    sousMenu = False     #Cette variable est vraie quand le joueur rentre dans le sous-menu et est fausse dans le cas inverse

    window.fill(WHITE)
    
    font1 = pygame.font.SysFont('Courier', 27)    #Je crée les polices d'écritures dont j'ai besoin et les assigne à une variable
    font2 = pygame.font.SysFont('Courier', 20)
    font3 = pygame.font.SysFont('Courier', 23)
    font4 = pygame.font.SysFont('Courier', 19)
    
    window.blit(font2.render("Votre argent : {0}".format(player.gold), False,(0,0,0)), (12,478))     #Je dessine le menu de marchand
    window.blit(spr_menu,(30,30))
    window.blit(spr_curseur,(80,45))
    window.blit(font1.render('ACHETER', False, (255,255,255)),(102,45))

    loop = True
    
    while loop:

        for event in pygame.event.get():
            if event.type == QUIT:        #Cette boucle sert à quitter la fenêtre si le joueur clique sur la croix
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.KEYDOWN :   #Cette boucle sert à détecter si une touche est pressée
                if event.key != pygame.K_RETURN and event.key != pygame.K_DOWN and event.key != pygame.K_UP and event.key != pygame.K_ESCAPE : #Cette boucle sert à ce qu'il ne se passe rien si le joueur appuie sur une touche autre que celles qui sont utiles (en raison de certains bugs)
                    pass
                    
                if event.key == pygame.K_RETURN and sousMenu == False :                     #Cette boucle sert à afficher le sous-menu
                    window.blit(spr_menu,(30,30))
                    window.blit(font1.render('ACHETER', False, (255,255,255)),(102,45))
                    window.blit(spr_curseur,(40,114))
                    window.blit(font2.render("Epée en fer", False,(255,255,255)),(62,118))
                    window.blit(font2.render("Katana Légendaire", False,(255,255,255)),(62,148))
                    window.blit(font2.render("Potion de vie", False,(255,255,255)),(62,178))
                    cursor = 1
                
                if event.key == pygame.K_DOWN :   #Ces deux boucles servent à modifier la valeur de la variable cursor si le joueur appuie sur les flèches du haut ou du bas
                    cursor += 2
                if event.key == pygame.K_UP :
                    cursor -= 2
                
                if cursor > 5 :      #Ces deux boucles servent à encadrer la variable cursor
                    cursor = 1
                if cursor < 0 :
                    cursor = 5
                
                if cursor == 1 :                                                                #Ces trois boucles servent à dessiner le curseur à des endroits différents en fonction de la valeur de la variable cursor
                    window.blit(spr_menu,(30,30))
                    window.blit(font1.render('ACHETER', False, (255,255,255)),(102,45))
                    window.blit(spr_curseur,(40,114))
                    window.blit(font2.render("Epée en fer", False,(255,255,255)),(62,118))
                    window.blit(font2.render("100", False,(255,255,255)),(202,143))
                    window.blit(spr_coin,(237,143))
                    window.blit(font2.render("Katana Légendaire", False,(255,255,255)),(62,168))
                    window.blit(font2.render("250", False,(255,255,255)),(202,193))
                    window.blit(spr_coin,(237,193))
                    window.blit(font2.render("Potion de vie", False,(255,255,255)),(62,218))
                    window.blit(font2.render("30", False,(255,255,255)),(202,243))
                    window.blit(spr_coin,(225,243))
                if cursor == 3 :
                    window.blit(spr_menu,(30,30))
                    window.blit(font1.render('ACHETER', False, (255,255,255)),(102,45))
                    window.blit(spr_curseur,(40,164))
                    window.blit(font2.render("Epée en fer", False,(255,255,255)),(62,118))
                    window.blit(font2.render("100", False,(255,255,255)),(202,143))
                    window.blit(spr_coin,(237,143))
                    window.blit(font2.render("Katana Légendaire", False,(255,255,255)),(62,168))
                    window.blit(font2.render("250", False,(255,255,255)),(202,193))
                    window.blit(spr_coin,(237,193))
                    window.blit(font2.render("Potion de vie", False,(255,255,255)),(62,218))
                    window.blit(font2.render("30", False,(255,255,255)),(202,243))
                    window.blit(spr_coin,(225,243))
                if cursor == 5 :
                    window.blit(spr_menu,(30,30))
                    window.blit(font1.render('ACHETER', False, (255,255,255)),(102,45))
                    window.blit(spr_curseur,(40,214))
                    window.blit(font2.render("Epée en fer", False,(255,255,255)),(62,118))
                    window.blit(font2.render("100", False,(255,255,255)),(202,143))
                    window.blit(spr_coin,(237,143))
                    window.blit(font2.render("Katana Légendaire", False,(255,255,255)),(62,168))
                    window.blit(font2.render("250", False,(255,255,255)),(202,193))
                    window.blit(spr_coin,(237,193))
                    window.blit(font2.render("Potion de vie", False,(255,255,255)),(62,218))
                    window.blit(font2.render("30", False,(255,255,255)),(202,243))
                    window.blit(spr_coin,(225,243))
                    
                if event.key == pygame.K_ESCAPE :
                    if sousMenu == True :             #Cette boucle sert à revenir en arrière dans le menu
                        window.blit(spr_menu,(30,30))
                        window.blit(spr_curseur,(80,45))
                        window.blit(font1.render('ACHETER', False, (255,255,255)),(102,45))
                        sousMenu = False
                    else :                   #Cette boucle sert à quitter le menu
                        loop = False
                    
                if event.key == pygame.K_RETURN and sousMenu == True and cursor == 1 :                #Ces trois boucles servent à acheter les objets et à verifier si le joueur a assez d'argent et s'il n'a pas déjà ces objets
                    if player.weapon.name == 'Epée en fer' :
                        window.blit(font2.render('Vous possédez déjà', False, (255,255,255)),(48,327))
                        window.blit(font2.render('cette arme', False, (255,255,255)),(98,347))
                    elif player.gold < 100 :
                        window.blit(font4.render("Pas assez d'argent", False, (255,255,255)),(54,347))
                    else :
                        window.blit(font3.render('Epée Achetée !', False, (255,255,255)),(58,343))
                        player.weapon = weapon(name='Epée en fer', damage = 10, skill = 'Thunderstruck', tempsCd = 5)
                        player.gold -= 100
                        levelWeapon = 0
                        pygame.draw.rect(window,WHITE,(10,460,240,50))
                        window.blit(font2.render("Votre argent : {0}".format(player.gold), False,(0,0,0)), (12,478))
                if event.key == pygame.K_RETURN and sousMenu == True and cursor == 3 :
                    if player.weapon.name == 'Katana Légendaire' :
                        window.blit(font2.render('Vous possédez déjà', False, (255,255,255)),(48,327))
                        window.blit(font2.render('cette arme', False, (255,255,255)),(98,347))
                    elif player.gold < 250 :
                        window.blit(font4.render("Pas assez d'argent", False, (255,255,255)),(54,347))
                    else :
                        window.blit(font3.render('Katana Acheté !', False, (255,255,255)),(52,343))
                        player.weapon = weapon(name='Katana Légendaire', damage = 15 , skill = 'Thunderstruck', tempsCd = 5)
                        player.gold -= 250
                        levelWeapon = 0
                        pygame.draw.rect(window,WHITE,(10,460,240,50))
                        window.blit(font2.render("Votre argent : {0}".format(player.gold), False,(0,0,0)), (12,478))
                if event.key == pygame.K_RETURN and sousMenu == True and cursor == 5 :
                    if player.backpack.potion == 5 :
                        window.blit(font2.render('Vous possédez déjà', False, (255,255,255)),(48,327))
                        window.blit(font2.render('5 potions', False, (255,255,255)),(98,347))
                    elif player.gold < 30 :
                        window.blit(font4.render("Pas assez d'argent", False, (255,255,255)),(54,347))
                    else :
                        window.blit(font3.render('Potion Achetée !', False, (255,255,255)),(45,343))
                        player.backpack.potion += 1
                        player.gold -= 30
                        pygame.draw.rect(window,WHITE,(10,460,240,50))
                        window.blit(font2.render("Votre argent : {0}".format(player.gold), False,(0,0,0)), (12,478))
                
                if event.key == pygame.K_RETURN and sousMenu == False :  #Cette boucle sert au programme de savoir si le joueur est dans le sous-menu ou non (cette boucle est à la fin car sinon le programme ne marche pas correctement)
                    sousMenu = True

        pygame.display.update()   #Cette commande sert à actualiser la fenêtre de jeu

