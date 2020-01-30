from weapon import weapon
from backpack import backpack
from ennemy import *

class character :
    """Classe définissant un personnage caractérisé par :
        -name ,le nom du personnage
        -hp, les points de vie du personnage
        -weapon, une arme attribué au personnage
        -life, un booleen qui permet de savoir si il est en vie
        
    Ses méthodes sont :
        -presentation, qui présente les différnets attributs du personnage
        -takeDamage, qui permet au personnage de perdre de la vie
        -dealDamage, qui permet d'attaquer un ennemi et de lui faire perdre de la vie"""
    
    def __init__(self,name="Michel",hp = 100,weapon = weapon(),backpack = backpack(),life = True,target = 2):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.backpack = backpack
        self.life = life
        self.target = target
        
    def presentation(self):
        print("Je m'appelle {0}, j'ai {1} pts de vie et mon arme est {2} (qui fait {3} pts de dégats). J'ai {4} potions.\n"\
              .format(self.name,self.hp,self.weapon.name,self.weapon.damage,self.backpack.potion))
    
    def takeDamage(self,damage):
        self.hp -= damage
        if self.hp <= 0 :
            print("{0} est mort !".format(self.name))
            self.hp = 0
            self.life = False
        else :
            print("{0} a perdu {1} pts de vie ! Il lui en reste {2}.".format(self.name,damage,self.hp))
    
    def dealDamage(self):
        ennemy.listEnnemy[self.target].takeDamage(self.weapon.damage)
        
    def dealSkillDamage(self,ennemy,damage = 5):
        ennemy.takeDamage(damage)
        
    def useSkill(self):
        if self.weapon.skill == 'None' :
            print("Rien ne se passe !")
        if self.weapon.skill == 'Thunderstruck' :
            dealSkillDamage(gobelin,10)
            
    def changeTarget(self,target):
        self.target = target
            

    