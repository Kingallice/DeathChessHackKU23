import pygame as pg
import sys
from Chess.chessManager import ChessManager
import chess

board = ChessManager()
bg_color = (0,0,255) #blue
window = pg.display.set_mode()
pg.display.set_caption("DEATH CHESS")
pg.display.update()
pg.display.flip()

#black images
background = pg.image.load("board.png")
RookB = pg.image.load("Images/Pieces/CHiss.png")
BishopB = pg.image.load("Images/Pieces/BishopB.png")
KnightB = pg.image.load("Images/Pieces/KnightB.png")
KingB = pg.image.load("Images/Pieces/KingB.png")
QueenB = pg.image.load("Images/Pieces/QueenB.png")
PawnB = pg.image.load("Images/Pieces/Pwned.png")

#white images
RookW = pg.image.load("")
BishopW = pg.image.load("")
KnightW = pg.image.load("")
KingW = pg.image.load("")
QueenW = pg.image.load("")
PawnW = pg.image.load("")

#highlights current square of mouse
def highlight_square(pos):
    for x in range(window.get_width()//4,1160,100):
        increase = 0
        for y in range(0,828,103):
            increase += 0.5
            if pos[0] > x and pos[0] < x + 100:
                if pos[1] > y and pos[1] < y + 103 + increase:
                    square = pg.Surface((100,103 + increase), pg.SRCALPHA)
                    square.fill((255,255,0,75))
                    window.blit(square,(x,y))

def update_board(board):
    state = board.getFen()
    print(state)
    x = window.get_width()//4
    y = 0
    for piece in range(len(state)):

        if state[piece] == '/':     #goes to next row
            y += 103.5
            x = window.get_width()//4
            continue
        for num in range(1,9):      #skips empty squares
            if state[piece] == num:
                for none in range(num):
                    x += 100
        #displays black pieces
        if state[piece] == 'r':
            window.blit(RookB, (x,y))
        if state[piece] == 'b':
            window.blit(BishopB, (x,y))
        if state[piece] == 'n':
            window.blit(KnightB, (x,y))
        if state[piece] == 'k':
            window.blit(KingB, (x,y))
        if state[piece] == 'q':
            window.blit(QueenB, (x,y))
        if state[piece] == 'p':
            window.blit(PawnB, (x,y))

        #displays white pieces
        if state[piece] == 'R':
            window.blit(RookW, (x,y))
        if state[piece] == 'B':
            window.blit(BishopW, (x,y))
        if state[piece] == 'N':
            window.blit(KnightW, (x,y))
        if state[piece] == 'K':
            window.blit(KingW, (x,y))
        if state[piece] == 'Q':
            window.blit(QueenW, (x,y))
        if state[piece] == 'P':
            window.blit(PawnW, (x,y))

        x += 100

while True:
    pos = pg.mouse.get_pos()
    window.fill(bg_color)
    window.blit(background, (window.get_width()/4,0))
    update_board(board)
    highlight_square(pos)
    pg.display.update()
    pg.display.flip()

    for event in pg.event.get():  #event to quit the game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONUP: #event to get square/piece coordinates
            clicked_pos = pos
            print(pos)