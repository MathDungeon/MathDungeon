class backpack :
    
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
        
        