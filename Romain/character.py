from weapon import weapon
from backpack import backpack

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
    
    def __init__(self,name="Michel",hp = 100,weapon = weapon(),backpack = backpack(),life = True):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.backpack = backpack
        self.life = life
        
    def presentation(self):
        print("Je m'appelle {0}, j'ai {1} pts de vie et mon arme est {2} (qui fait {3} pts de dégats). J'ai {4} potions."\
              .format(self.name,self.hp,self.weapon.name,self.weapon.damage,self.backpack.potion))
    
    def takeDamage(self,damage):
        self.hp -= damage
        if self.hp <= 0 :
            print("{0} est mort !".format(self.name))
            self.hp = 0
            self.life = False
        else :
            print("{0} a perdu {1} pts de vie ! Il lui en reste {2}.".format(self.name,damage,self.hp))
    
    def dealDamage(self,ennemy):
        ennemy.takeDamage(self.weapon.damage)
        
    