from random import randint

class ennemy :
    
    """Un classe définissant un ennemi caractérisé par :
        -name, le nom de l'ennemi
        -damage, les dégats que l'ennemi inflige
        -hp, les points de vie de l'ennemi
        -life, un booleen qui indique si l'ennemi est en vie
        
    Ses méthodes sont :
        -dealDamage, qui inflige des dégats
        -takeDamage, qui permet de se prendre des dégats"""
        
    listEnnemy = [0,0,0,0,0] 
    
    def __init__(self,position,name = "Gobelin",damage = 10,hp = 30,summon = 0,count = 0,life = True):
        self.position = position
        self.name = name
        self.damage = damage
        self.hp = hp
        self.life = life
        self.summon = summon
        self.count = count
        ennemy.listEnnemy[self.position] = self
     
        
    def presentation(self) :
        print("{0} fait {1} dégats, a {2} pts de vie à l'emplacement {3}".format(self.name,self.damage,self.hp,self.position))
    
    def presentationEnnemy(cls) :
        for i in ennemy.listEnnemy :
            if i != 0 :
                i.presentation()
    presentationEnnemy = classmethod(presentationEnnemy)
    
    
    
    def takeDamage(self,damage):
        self.hp -= damage
        if self.hp <= 0 :
            print("{0} a perdu {1} pts de vie !".format(self.name,damage))
            print("{0} est mort !".format(self.name))
            self.hp = 0
            self.life = False
            ennemy.listEnnemy[self.position] = 0
        else :
            print("{0} a perdu {1} pts de vie ! Il lui en reste {2}.".format(self.name,damage,self.hp))

       
    def dealDamage(self,character):
        character.takeDamage(self.damage)
    
    def summonEnnemy(self,position) :
        if self.summon == 'Bat' :
            print("Le comte Vladimir a invoqué une chauve-souris à l'emplacement {0} !".format(position))
            ennemy.listEnnemy[position] = ennemy(position,"Chauve-souris",5,10)
            

                
    
    def action(self,personnage) :
        
        if self.name == "Gobelin" or self.name == "Squelette" or self.name == "Chauve-souris" :
            self.dealDamage(personnage)
        
        if self.name == "Troll" :
            
            if self.count == 0 :
                self.dealDamage(personnage)
                self.count = 1
            else : 
                self.count -= 1
        
        if self.name == "Comte Vladimir" :
            
            if len([i for i in ennemy.listEnnemy if i != 0]) < 3 and randint(1,10) < 5 :
                count = 0
                for pos,i in enumerate(ennemy.listEnnemy):
                    if i == 0 :
                        self.summonEnnemy(pos)
                        count += 1
                    if count == 2:
                        break
                        
            else :
                self.dealDamage(personnage)
            
        
            
            
    