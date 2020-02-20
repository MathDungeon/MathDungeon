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
    
    def __init__(self,position,name = "Gobelin",damage = 20,hp = 30,life = True):
        self.position = position
        self.name = name
        self.damage = damage
        self.hp = hp
        self.life = life
        ennemy.listEnnemy[self.position] = self
        
    def presentation(self) :
        print("{0} fait {1} dégats, a {2} pts de vie à l'emplacement {3}".format(self.name,self.damage,self.hp,self.position))
    
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
       
    def presentationEnnemy(cls) :
        for i in ennemy.listEnnemy :
            if i != 0 :
                i.presentation()
    presentationEnnemy = classmethod(presentationEnnemy)