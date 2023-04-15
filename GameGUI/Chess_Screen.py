#Date: 4-14-23
#Author: Luke Slizoski
#This file is the gui for interactions with the board


import pygame as pg
import sys
from Chess.chessManager import ChessManager

board = ChessManager()
bg_color = (0,0,0) #black
window = pg.display.set_mode()
pg.display.set_caption("DEATH CHESS")
pg.display.update()
pg.display.flip()
letters = ['a','b','c','d','e','f','g','h']
numbers = ['8','7','6','5','4','3','2','1']
move_list = []

#black images
background = pg.image.load("board.png")
RookB = pg.image.load("Images/Pieces/CHiss.png")
BishopB = pg.image.load("Images/Pieces/BishopB.png")
KnightB = pg.image.load("Images/Pieces/Horse_Girl_Black.png")
KingB = pg.image.load("Images/Pieces/KingB.png")
QueenB = pg.image.load("Images/Pieces/QueenB.png")
PawnB = pg.image.load("Images/Pieces/Pwned_Black.png")

#white images

RookW = pg.image.load("Images/Pieces/w_rook.png")
BishopW = pg.image.load("Images/Pieces/w_bishop.png")
KingW = pg.image.load("Images/Pieces/w_king.png")
QueenW = pg.image.load("Images/Pieces/w_queen.png")
KnightW = pg.image.load("Images/Pieces/Horse_Girl_White.png")
PawnW = pg.image.load("Images/Pieces/Pwned_White.png")

#highlights current square of mouse
def highlight_square():
    pos = pg.mouse.get_pos()
    for x in range(window.get_width()//4,1160,100):
        increase = 0
        for y in range(0,828,103):
            increase += 0.5
            if pos[0] > x and pos[0] < x + 100:
                if pos[1] > y and pos[1] < y + 103 + increase:
                    square = pg.Surface((100,103 + increase), pg.SRCALPHA)
                    square.fill((255,255,0,75))
                    window.blit(square,(x,y))

#updates the pieces on the board
def update_board(board):
    state = board.getFen()
    x = window.get_width()//4
    y = 0
    for piece in range(len(state)):
        if state[piece].isnumeric():
            x += (int(state[piece])-1)*100
        if state[piece] == '/':     #goes to next row
            y += 103.5
            x = window.get_width()//4
            continue

        #displays black pieces
        if state[piece] == 'r':
            window.blit(RookB, (x,y))
        elif state[piece] == 'b':
            window.blit(BishopB, (x,y))
        elif state[piece] == 'n':
            window.blit(KnightB, (x,y))
        elif state[piece] == 'k':
            window.blit(KingB, (x,y))
        elif state[piece] == 'q':
            window.blit(QueenB, (x,y))
        elif state[piece] == 'p':
            window.blit(PawnB, (x,y))

        #displays white pieces
        elif state[piece] == 'R':
            window.blit(RookW, (x,y))
        elif state[piece] == 'B':
            window.blit(BishopW, (x,y))
        elif state[piece] == 'K':
            window.blit(KingW, (x,y))
        elif state[piece] == 'Q':
            window.blit(QueenW, (x,y))
        elif state[piece] == 'P':
            window.blit(PawnW, (x,y))
        elif state[piece] == 'N':
            window.blit(KnightW, (x,y))
        x += 100

#highlights currently clicked on square
def clicked_highlighted_square():
    if not move_list:
        return
    first = move_list[-1]
    xcord = 360
    ycord = 0
    for letter in letters:
        if first[0] == letter:
            break
        xcord += 100

    for num in numbers:
        if first[1] == num:
            break
        ycord += 103.5
    if board.isOccupied(first[0]+first[1]):
        square2 = pg.Surface((100, 103), pg.SRCALPHA)
        square2.fill((255, 255, 0, 75))
        window.blit(square2, (xcord, ycord))

    if len(move_list) == 2:
        move(move_list[-2] + move_list[-1])
        move_list.clear()



#Makes only valid moves for player
def move(uciMove):
    if board.isLegalMove(uciMove):
        board.pushMove(uciMove)

#runs the game
while True:
    window.fill(bg_color)
    window.blit(background, (window.get_width()/4,0))
    update_board(board)
    highlight_square()
    clicked_highlighted_square()
    pg.display.update()
    pg.display.flip()

    for event in pg.event.get():  #event to quit the game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONUP: #event to get square/piece coordinates
            clicked_pos = pg.mouse.get_pos()
            uciMove = ''

            #records the letter rank of clicked square
            for x in range(1,9):
                if clicked_pos[0] > window.get_width() / 4 and clicked_pos[0] < window.get_width() /4 + x * 100:
                    if clicked_pos[1] < 828 and clicked_pos[1] > 0:
                        uciMove += letters[x-1]
                        break

            # records the number rank of clicked square
            for y in range(1,9):
                if clicked_pos[0] < window.get_width() / 4 + 800 and clicked_pos[0] > window.get_width() / 4:
                    if clicked_pos[1] > 0 and clicked_pos[1] < y * 103.5:
                        uciMove += numbers[y-1]
                        break


            move_list.append(uciMove)

