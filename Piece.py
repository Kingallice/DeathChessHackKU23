import pygame as pg
import chess

#AUTHOR _ GUY WHO IS INSANE
class Piece(pg.sprite):
    def __init__(self, team, image, x, y):
        self.team = team
        self.image = image
        self.location = (x, y)

    def capture(self, capturing_piece, captured_piece):
        win_loss = self.minigame(capturing_piece, captured_piece)
        if win_loss==True:
            captured_piece.remove()


    def minigame(self, capturing_piece, captured_piece):
        pass

    def set_loc(self, newx, newy):
        self.x = newx
        self.y = newy
    def remove_piece(self):
        pass

class Pawn(Piece):
    def __init__(self, team, x, y, movement):
        super.__init__(team, x, y)
        self.movement = movement

    def move(self, clickpointx, clickpointy, x, y):
        if clickpointx == x and (clickpointy == y+103 or clickpointy == y+206):
            self.set_loc(clickpointy, clickpointx)


bp = Piece("b", "p", 0, 0, 0)