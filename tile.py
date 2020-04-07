import functions as f
import constants as const
import pygame

class tile:
    """
    Define:
    Coordinates
    If tile has been visited yet
    What does the tile contains
    """
    
    def __init__(self,coordinates,isVisible=False,content=None):
        
        (x,y) = coordinates
        self.x = x
        self.y = y
        self.isVisible = isVisible
        self.content = content
        self.tileDraw()
        const.mape[self.y][self.x] = self
        self.up = const.mape[self.y - 1][self.x]
        self.down = const.mape[self.y + 1][self.x]
        self.left = const.mape[self.y][self.x - 1]
        self.right = const.mape[self.y][self.x + 1]
        if self.up:
            self.up.down = self
        if self.down:
            self.down.up = self
        if self.left:
            self.left.right = self
        if self.right:
            self.right.left = self
        if (self.x,self.y)==(f.player.x,f.player.y):
            f.player.tile = self

    def clear(self):
        const.mape[self.y][self.x] = None
        del self

    def __repr__(self):
        if self.content:
            return "{0} at {1},{2}".format(self.content,self.x,self.y)
        else:
            return "Case vide at {0},{1}".format(self.x,self.y)
    
    def tileDraw(self):
        global window
        if self.isVisible:
            f.window.blit(const.visibleTileSprite,((self.x*32),(self.y*32)))
            if self.content == "Boss" and not(self.x == f.player.x and self.y == f.player.y):
                f.window.blit(const.bossSprite,((self.x*32),(self.y*32)))
            if self.content == "Shop" and not(self.x == f.player.x and self.y == f.player.y):
                f.window.blit(const.shopSprite,((self.x*32),(self.y*32)))
            if self.content == "Defeated_Boss" and not(self.x == f.player.x and self.y == f.player.y):
                f.window.blit(const.trapdoorSprite,((self.x*32),(self.y*32)))
        else:
            f.window.blit(const.notVisibleTileSprite,((self.x*32),(self.y*32)))

    def reveal(self):
        self.isVisible = True
    
    def discover(self):
        for i in (self.up,self.down,self.left,self.right):
            if i:
                i.reveal()

    def interact(self):
        if self.content:
            global window
            temp = {"Boss":"Oulala", "Shop":"Marchander","Defeated_Boss":"Etage suivant"}
            text = const.font.render(temp[self.content],True,const.colorBlack)
            f.window.blit(const.keyESprite,(416,370))
            f.window.blit(text,(448,371))