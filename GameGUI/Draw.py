import pygame as pg
class Draw:

    def __init__(self):
        self.font = pg.font.SysFont('Arial', 100)
        self.drawText = self.font.render("It's a Draw", True, ((220,220,220)))

    def draw(self,window):
        window.blit(self.drawText,(window.get_width()/2 - 300, window.get_height()/2 - 50))

