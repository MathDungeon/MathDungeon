from random import randint
from constantFight import *

class ennemy :
    
    """Initialisation de la classe ennemy. 
        Elle contient une variable de classe, listEnnemy, qui permet de compter et ordonner les ennemis en vie lors d'un combat.
            C'est dans cette liste que nous créerons tous les ennemis, les supprimerons, compterons combien sont en vie...
        Elle a plusieurs arguments :
            - position, qui correspond à sa position dans listEnnemy.
            - name, qui correspond au nom de l'ennemi et donc à son type (Gobelin, Chauve-souris, etc...)
            - damage, qui correspond aux dégats infligés à chaque attaque
            - hp, qui correspond à ses points de vie
            - summon, qui est un string suivant si l'ennemi va invoquer d'autres ennemis, et qui indique quel leur type
            - count, qui permet de donner un délai aux attaques afin qu'il n'attaque pas forcément tous les tours.
            - life, qui est un booléen True si l'ennemi est en vie ou bien False si il est mort
            - apparition, un booléen qui permet d'empêcher l'ennemi d'attaquer le tour de son summon.
        Elle a plusieurs méthodes :
            - takeDamage, qui permet de faire perdre des points de vie à l'ennemi quand on l'attaque
            - dealDamage, qui appelle la méthode takeDamage du personnage
            - summonEnnemy, qui invoque d'autres ennemis suivant l'argument summon.
            
        
    """ 
    
    #Variable de classe
    listEnnemy = [0,0,0,0,0] 
    
    
    #Initialisation de la classe
    def __init__(self,position,name,damage,hp,summon,count,life = True,apparition = False):
        self.position = position
        self.name = name
        self.damage = damage
        self.hp = hp
        self.life = life
        self.summon = summon
        self.count = count
        self.apparition = apparition
        ennemy.listEnnemy[self.position] = self    
    
    
    #Méthodes de classe
    def takeDamage(self,damage):
        
        #Pour les 3 formes de boss finales, la mort provoque le passage à la phase suivante :
        #Ainsi on limite le nombre de points de vie perdus, et la mort provoque le changement de phase
        if self.name == "Msmoke_vladimir" :
            
            self.hp -= damage
        
            if self.hp <= 80 :  # Si l'ennemi depasse le seuil des 80 hps :
                self.hp = 80
                self.name = "Msmoke2"  #On change son nom, qui changera aussi ses actions
        
        elif self.name == "Msmoke_sorciere" :
            
            self.hp -= damage
        
            if self.hp <= 40 :  # Idem
                self.hp = 40
                self.name = "Msmoke3"  
                
        elif self.name == "Msmoke_ogre" :
            
            self.hp -= damage
        
            if self.hp <= 0 :  # Idem
                self.hp = 0
                self.name = "Msmoke4"
        
        elif self.name != "Msmoke" and self.name != "Msmoke2" and self.name != "Msmoke3":    #Msmoke est le boss final, il ne peut pas prendre de dégâts sous sa forme fumée
        
            self.hp -= damage
        
            if self.hp <= 0 :  # Si l'ennemi meurt :
                self.hp = 0
                self.life = False
                ennemy.listEnnemy[self.position] = 0
               
            
    def dealDamage(self,character):
        character.takeDamage(self.damage)
    
    def summonEnnemy(self,position) :
        
        if self.summon == 'Bat' :
            ennemy.listEnnemy[position] = ennemy(position,name = nameBat,hp = hpBat,damage = damageBat,summon = summonBat, count = countBat)
            
        if self.summon == 'Spider' :
            ennemy.listEnnemy[position] = ennemy(position,name = nameSpider,hp = hpSpider,damage = damageSpider,summon = summonSpider, count = countSpider)
            
        if self.summon == 'Gobelin' :
            ennemy.listEnnemy[position] = ennemy(position,name = nameGobelin,hp = hpGobelin,damage = damageGobelin,summon = summonGobelin, count = countGobelin)
