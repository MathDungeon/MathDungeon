class ennemy :
    
    """Un classe définissant un ennemi caractérisé par :
        -name, le nom de l'ennemi
        -damage, les dégats que l'ennemi inflige
        -hp, les points de vie de l'ennemi
        -life, un booleen qui indique si l'ennemi est en vie
        
    Ses méthodes sont :
        -dealDamage, qui inflige des dégats
        -takeDamage, qui permet de se prendre des dégats"""
    
    def __init__(self,name = "Gobelin",damage = 20,hp = 30,life = True):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.life = life
        
    def takeDamage(self,damage):
        self.hp -= damage
        if self.hp <= 0 :
            print("{0} a perdu {1} pts de vie !".format(self.name,damage))
            print("{0} est mort !".format(self.name))
            self.hp = 0
            self.life = False
        else :
            print("{0} a perdu {1} pts de vie ! Il lui en reste {2}.".format(self.name,damage,self.hp))
            
    def dealDamage(self,character):
        character.takeDamage(self.damage)
    