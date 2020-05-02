# -*- coding: utf-8 -*-
import pygame, sys                   #J'importe les modules et les fichiers dont j'ai besoin
from pygame.locals import *
from ennemy import *
from functions import * 
from constantFight import *
from character import *                                    

spr_menu = pygame.image.load("Sprites/menu.png")                        #J'importe les images dont j'ai besoin et je les associe à une variable
spr_curseur = pygame.image.load("Sprites/test_curseur_jaune.png")

def menuForgeron():
    pygame.init()   #On initialise pygame

    window = pygame.display.set_mode((928,512))   #On crée la fenêtre de jeu

    WHITE = (255,255,255)                                                                         #Je crée les variables que j'utiliserai plus tard
    personnage = character()
    levelWeapon = 0
    gold = 500
    personnage.weapon = weapon(name='Epée rouillée', damage=5, skill='Thunderstruck', tempsCd=5)
    sousMenu = False

    window.fill(WHITE)
    
    font1 = pygame.font.SysFont('Courier', 27)    #Je crée les polices d'écritures dont j'ai besoin et les assigne à une variable
    font2 = pygame.font.SysFont('Courier', 20)
    font3 = pygame.font.SysFont('Courier', 23)
    
    window.blit(spr_menu,(30,30))                                        #Je dessine le menu du forgeron
    window.blit(spr_curseur,(60,45))
    window.blit(font1.render('AMELIORER', False, (255,255,255)),(82,45))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:            #Cette boucle sert à quitter la fenêtre si le joueur clique sur la croix
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN :  #Cette boucle sert à détecter si une touche est pressée
                if event.key != pygame.K_RETURN and event.key != pygame.K_DOWN and event.key != pygame.K_UP and event.key != pygame.K_ESCAPE :  #Cette boucle sert à ce qu'il ne se passe rien si le joueur appuie sur une touche autre que celles qui sont utiles (en raison de certains bugs)
                    pass
                    
                if event.key == pygame.K_RETURN and sousMenu == False :        #Cette boucle sert à afficher le sous-menu
                    window.blit(spr_menu,(30,30))
                    window.blit(font1.render('AMELIORER', False, (255,255,255)),(82,45))
                    window.blit(spr_curseur,(40,114))
                    if personnage.weapon.name == 'Epée rouillée' :
                        window.blit(font2.render('Epée rouilée', False, (255,255,255)),(62,118))
                    elif personnage.weapon.name == 'Epée en fer' :
                        window.blit(font2.render('Epée en fer', False, (255,255,255)),(62,118))
                    elif personnage.weapon.name == 'Katana Légendaire' :
                        window.blit(font2.render('Katana Légendaire', False, (255,255,255)),(62,118))
                    
                if event.key == pygame.K_ESCAPE :
                    if sousMenu == True :                 #Cette boucle sert à revenir en arrière dans le menu
                        window.blit(spr_menu,(30,30))
                        window.blit(spr_curseur,(60,45))
                        window.blit(font1.render('AMELIORER', False, (255,255,255)),(82,45))
                        sousMenu = False
                    else :                #Cette boucle sert à quitter le menu
                        window.fill(WHITE)
                    
                if event.key == pygame.K_RETURN and sousMenu == True :   #Cette boucle sert à améliorer l'arme et à vérifier si le joueur a assez d'argent et si l'arme n'est pas déjà améliorer au maximum
                    levelWeapon += 1
                    if levelWeapon > 3:
                        levelWeapon = 3
                        window.blit(spr_menu,(30,30))
                        window.blit(font1.render('AMELIORER', False, (255,255,255)),(82,45))
                        window.blit(spr_curseur,(40,114))
                        if personnage.weapon.name == 'Epée rouillée' :
                            window.blit(font2.render('Epée rouilée', False, (255,255,255)),(62,118))
                        elif personnage.weapon.name == 'Epée en fer' :
                            window.blit(font2.render('Epée en fer', False, (255,255,255)),(62,118))
                        elif personnage.weapon.name == 'Katana Légendaire' :
                            window.blit(font2.render('Katana Légendaire', False, (255,255,255)),(62,118))
                        window.blit(font2.render("L'arme ne peut pas", False, (255,255,255)),(42,205))
                        window.blit(font2.render("être plus améliorée", False, (255,255,255)),(42,225))
                    elif gold < 70 :
                        window.blit(font4.render("Pas assez d'argent", False, (255,255,255)),(54,347))
                    else :
                        personnage.weapon.damage += 3
                        gold -= 70
                        window.blit(spr_menu,(30,30))
                        window.blit(font1.render('AMELIORER', False, (255,255,255)),(82,45))
                        window.blit(spr_curseur,(40,114))
                        if personnage.weapon.name == 'Epée rouillée' :
                            window.blit(font2.render('Epée rouilée', False, (255,255,255)),(62,118))
                        elif personnage.weapon.name == 'Epée en fer' :
                            window.blit(font2.render('Epée en fer', False, (255,255,255)),(62,118))
                        elif personnage.weapon.name == 'Katana Légendaire' :
                            window.blit(font2.render('Katana Légendaire', False, (255,255,255)),(62,118))
                        window.blit(font2.render("L'arme a été", False, (255,255,255)),(42,205))
                        window.blit(font2.render("améliorée", False, (255,255,255)),(42,225))
                        if levelWeapon == 1 :
                            window.blit(font2.render("(lvl: 1)", False, (255,255,255)),(42,265))
                        elif levelWeapon == 2 :
                            window.blit(font2.render("(lvl: 2)", False, (255,255,255)),(42,265))
                        elif levelWeapon == 3 :
                            window.blit(font2.render("(lvl: 3)", False, (255,255,255)),(42,265))
                        
                    
                if event.key == pygame.K_RETURN and sousMenu == False :    #Cette boucle sert au programme de savoir si le joueur est dans le sous-menu ou non (cette boucle est à la fin car sinon le programme ne marche pas correctement)
                    sousMenu = True
                
        pygame.display.update()   #Cette commande sert à actualiser la fenêtre de jeu

menuForgeron()
