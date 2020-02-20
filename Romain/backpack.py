class backpack :
    
    def __init__(self,potion = 5) :
        self.potion = potion
        
    def usePotion (self,character) :
        self.potion -= 1
        character.hp += 30
        print("Tu te soignes de 30 pts de vie ! Tu as {0} pts de vie et {1} potions.".format(character.hp,self.potion))
        
        
        
        