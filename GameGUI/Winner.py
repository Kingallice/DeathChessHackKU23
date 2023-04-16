import pygame as pg
class Winner:

    def __init__(self, winner):
        self.font = pg.font.SysFont('Arial', 100)
        if winner:
            color = "Black"
        else:
            color = "White"
        self.winText = self.font.render("Congrats " + color, True, ((144, 238, 144)))

    def draw(self,window):
        window.blit(self.winText,(window.get_width()/2 - 300, window.get_height()/2 - 50))

