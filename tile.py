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
    
    def tileDraw(self):
        global window
        if self.isVisible:
            f.window.blit(const.visibleTileSprite,((self.x*32),(self.y*32)))
            if self.content == "Boss" and not(self.x == f.xPlayer and self.y == f.yPlayer):
                f.window.blit(const.bossSprite,((self.x*32),(self.y*32)))
            if self.content == "Marchand" and not(self.x == f.xPlayer and self.y == f.yPlayer):
                f.window.blit(const.shop,((self.x*32),(self.y*32)))
        else:
            f.window.blit(const.notVisibleTileSprite,((self.x*32),(self.y*32)))

    def reveal(self):
        self.isVisible = True
    
    def discover(self):
        for i in (self.up,self.down,self.left,self.right):
            if i:
                i.reveal()