import pygame as pg
import chess

#AUTHOR _ GUY WHO IS INSANE
class Piece(pg.sprite):
    def __init__(self, team, type, movement, image, location):
        self.type = type
        self.movement = movement
        self.team = team
        self.image = image
        self.location = location

    def capture(self, capturing_piece, captured_piece):
        win_loss = minigame(capturing_piece, captured_piece)
        if win_loss==True:
            captured_piece.remove()


    def minigame(self, capturing_piece, captured_piece):
        pass

    def set_loc(self):
        self.location = -1000
    def remove_piece(self):
        self.piece



bp = piece("b", "p", 0, 0, 0)