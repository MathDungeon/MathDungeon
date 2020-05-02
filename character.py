"""
Code by Remi & Romain
"""

from ennemy import *
from romainFunctions import * 
from constantFight import *
import functions as f
import constants as const


class weapon : #Définition de notre classe Weapon
    
    """Initialisation de la classe Weapon.
        Elle a plusieurs arguments :
            - name, qui permet de nommer l'arme 
            - damage, qui définit les dégats infligés par attaque
            - skill, un string qui définit la compétence spéciale de l'arme
            - tempsCd, qui définit le délai de récupération de la compétence spéciale
        Elle a une méthode :
            - change, qui permet de changer les arguments de l'arme en contournant l'encapsulation, et en évitant de devoir remplacer l'arme.
                Je ne sais pas vraiment si cela est utile en vue de mon expérience de programmeur, mais je pense que cela peut être utile.
                
    """
    #Initialisation de la classe
    def __init__(self,name="Epée rouilée",damage=10,skill = 'Thunderstruck',tempsCd = 5): #La méthode constructeur
        self.damage = damage
        self.name = name
        self.skill = skill
        self.tempsCd = tempsCd
        self.cooldown = 0
    
    #Méthodes de classe
    def change(self,name = "Epee rouillé",damage = 10,skill = 'Thunderstruck',tempsCd = 5):
        self.damage = damage
        self.name = name
        self.skill = skill
        self.tempsCd = tempsCd
        
        
        
class backpack : #Définition de notre classe Backpack
    
    
    """Initialisation de la classe Backpack
        Elle a un argument :
            - potion, qui compte le nombre de potions possédées
        Elle a une méthode : 
            - usePotion, qui permet d'utiliser une potion afin de se soigner.
            
            PS: Cette classe ne sert actuellement que pour les potions mais s'appelle Backpack, 
                car j'avais envisagé de rajouter d'autres fonctionnalitées(Anti-Brulûre,etc...)
                Cependant, je n'ai pas eu le temps de rajouter ces autres fonctionnalitées, qui auraient été complexes à intégrer.
                
    """
        
    #Initialisation de la classe
    def __init__(self,potion = 5) :
        self.potion = potion
    
    #Méthodes de classe
    def usePotion (self,character) :
        
        if self.potion != 0 :  # Si il nous reste des potions
            self.potion -= 1
            if character.hp < 70 :
                character.hp += 30
            else :             # On arrondi les hps si ils dépassent les 100 hp.   
                character.hp = 100

class character :
    
    """Initialisation de la classe Character.
        Elle a plusieurs arguments :
            - name, qui définit le nom du personnage (un peu inutile mais bon...)
            - hp, qui définit les points de vie de notre personnage
            - weapon, qui donne une arme au personnage. 
            - backpack, qui donne des potions au personnage
            - life, un booléen qui regarde si le personnage est en vie
            - target, qui permet de cibler un ennemi spécifique (il définit l'emplacement de la listEnnemy que le personnage attaque)
        Elle a plusieurs méthodes :
            - takeDamage, qui permet de perdre des points de vie.
            - dealDamage, qui appelle la fonction takeDamage de l'ennemi.
            - dealSkillDamage, qui permet d'infliger des dégats différents de ceux du personnage avec sa compétence.
            - useSkill, qui permet d'utiliser sa compétence de son arme.
            - changeTarget, qui permet de changer l'argument target qui est appelé lors de l'attaque d'un ennemi en évitant l'encapsulation    
    
    """
    
    #Initialisation de la classe
    def __init__(self,name="Michel",hp = 100,weapon = weapon(damage = 120),backpack = backpack(),gold = 0,life = True,target = 2, coordinates = (14,7)):
        x,y = coordinates
        self.x = x
        self.y = y
        self.name = name
        self.hp = hp
        self.gold = gold
        self.weapon = weapon
        self.backpack = backpack
        self.life = life
        self.target = target
        self.x = x
        self.y = y
        self.tile = const.mape[self.y][self.x]
        
    
    #Méthodes de classe
    def takeDamage(self,damage):
        self.hp -= damage
        if self.hp <= 0 :  #Si l'ennemi meurt
            self.hp = 0
            self.life = False
        
    
    def dealDamage(self):
        ennemy.listEnnemy[self.target].takeDamage(self.weapon.damage)
    
    #RestezChezVous, et prenez soin de vous :)
    def dealSkillDamage(self,damage = 5):
        ennemy.listEnnemy[self.target].takeDamage(damage)
        
    def useSkill(self):
        if self.weapon.cooldown == 0 :   #Si la compétence de l'arme est rechargé
            self.weapon.cooldown = self.weapon.tempsCd  #Remettre le cooldown à la constante initial de temps définie
            if self.weapon.skill == 'Thunderstruck' :
                self.changeTarget(askTarget(self))
                self.dealSkillDamage(20)
                    
            
    def changeTarget(self,target):
        self.target = target
    
    def move(self,x,y):
        self.x = x
        self.y = y
        self.x = f.varFraming(self.x, 0, const.cWeight)
        self.y = f.varFraming(self.y, 0, const.cHeight)
        self.tile = const.mape[self.y][self.x]