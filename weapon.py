class weapon : #Définition de notre classe Arme
    """Classe définissant une arme caractérisée par : 
       - Son nom
       - Ses dégats"""
       
    """Ses méthodes :
        - presentation, qui affiche les atributs de l'arme (nom et dégats)
        - change, qui change l'arme en remplaçant ses attributs"""
    
    def __init__(self,name="Epée rouilée",damage=10): #La métohde constructeur
        self.damage = damage
        self.name = name
    
    def presentation(self):
        print("Cette arme est" , self.name , ", une arme qui possède" , self.damage , "points de dégats")
    
    def change(self,name = "Epee rouillé",damage = 10):
        self.damage = damage
        self.name = name
        
