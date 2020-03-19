from ennemy import *
from functions import *


class weapon : #Définition de notre classe Weapon
    
    """Cette classe défini une arme par : 
       - Un nom
       - Des dégats
       - Une compétence"""
       
    """Ses méthodes sont :
        - presentation, qui affiche dans la console les atributs de l'arme (nom et dégats)
        - change, qui change l'arme en remplaçant ses attributs """
    
    def __init__(self,name="Epée rouilée",damage=10,skill = 'Thunderstruck'): #La métohde constructeur
        self.damage = damage
        self.name = name
        self.skill = skill
    
    def presentation(self):
        print("Cette arme est" , self.name , ", une arme qui possède" , self.damage , "points de dégats et avec comme compétence :" ,self.skill)
    
    def change(self,name = "Epee rouillé",damage = 10,skill = 'Thunderstruck'):
        self.damage = damage
        self.name = name
        self.skill = skill
        
        
        
class backpack : #Définition de notre classe Backpack
    
    
    def __init__(self,potion = 5) :
        self.potion = potion
        
    def usePotion (self,character) :
        
        if self.potion != 0 :
            self.potion -= 1
            character.hp += 30
            if not self.potion == 0 :
                print("Tu te soignes de 30 pts de vie ! Tu as {0} pts de vie et {1} potions.".format(character.hp,self.potion))
            else :
                print("Tu te soignes de 30 pts de vie ! Tu n'as plus de potion.".format(character.hp))
        
        
        else :
            print("Tu n'as plus de potions !")
        
        
    

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
            print("{0} a perdu {1} pts de vie ! {0} est mort !".format(self.name,damage))
            self.hp = 0
            self.life = False
        else :
            print("{0} a perdu {1} pts de vie ! Il lui en reste {2}.".format(self.name,damage,self.hp))
    
    def dealDamage(self):
        ennemy.listEnnemy[self.target].takeDamage(self.weapon.damage)
        
    def dealSkillDamage(self,damage = 5):
        ennemy.listEnnemy[self.target].takeDamage(damage)
        
    def useSkill(self):
        if self.weapon.skill == 'None' :
            print("Rien ne se passe !")
        if self.weapon.skill == 'Thunderstruck' :
            self.changeTarget(askTarget(self))
            self.dealSkillDamage(20)
            
            
    def changeTarget(self,target):
        self.target = target
            
