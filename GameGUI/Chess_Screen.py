#Date: 4-14-23
#Author: Luke Slizoski
#This file is the gui for interactions with the board

import pygame as pg
import sys
import json
from Chess.chessManager import ChessManager

settings = json.loads(open("./Config/settings.dat", "r").read())

tempData = open("./Config/temp.dat", "r+b")
tempDataText = tempData.read()

board = ChessManager()
if len(tempDataText) > 0:
    board = ChessManager(tempDataText.decode())

bg_color = (0,0,0) #black
window = pg.display.set_mode(settings["currResolution"])
if settings["fullscreen"]:
    window = pg.display.set_mode((0,0), pg.FULLSCREEN)
pg.display.set_caption("DEATH CHESS")
pg.display.update()
pg.display.flip()
letters = ['a','b','c','d','e','f','g','h']
numbers = ['8','7','6','5','4','3','2','1']
move_list = []
print(window.get_height()//2 - 104)
background = pg.image.load("board.png")

#black images
RookB = pg.image.load("Images/Pieces/rookB.svg")
BishopB = pg.image.load("Images/Pieces/bishopB.svg")
KnightB = pg.image.load("Images/Pieces/knightB.svg")
KingB = pg.image.load("Images/Pieces/kingB.svg")
QueenB = pg.image.load("Images/Pieces/queenB.svg")
PawnB = pg.image.load("Images/Pieces/pawnB.svg")

#white images
RookW = pg.image.load("Images/Pieces/rookW.svg")
BishopW = pg.image.load("Images/Pieces/bishopW.svg")
KingW = pg.image.load("Images/Pieces/kingW.svg")
QueenW = pg.image.load("Images/Pieces/queenW.svg")
KnightW = pg.image.load("Images/Pieces/knightW.svg")
PawnW = pg.image.load("Images/Pieces/pawnW.svg")

yStart = (window.get_height() - background.get_height())//2
pieceSize = (100, 100)

def scaleImage(img, size):
    return pg.transform.smoothscale(img, size)

#highlights current square of mouse
def highlight_square():
    pos = pg.mouse.get_pos()
    for x in range(window.get_width()//4,1160,100):
        increase = 0
        for y in range(yStart,yStart+828,103):
            increase += 0.5
            if pos[0] > x and pos[0] < x + 100:
                if pos[1] > y and pos[1] < y + 103 + increase:
                    square = pg.Surface((100,103 + increase), pg.SRCALPHA)
                    square.fill((255,255,0,75))
                    window.blit(square,(x,y))

    #trying to get pawn promotion square highlight
    for x in range(window.get_width()//4 - 255, window.get_width()//4 - 154, 100):
        for y in range(window.get_height()//2, window.get_height()//2 +104, 103):
            if pos[0] > x and pos[0] < x + 100:
                if pos[1] > y and pos[1] < y + 103 + 0.5:
                    square = pg.Surface((100, 103 + 0.5), pg.SRCALPHA)
                    square.fill((255, 255, 0, 75))
                    window.blit(square, (x+28, y))

#updates the pieces on the board
def update_board(board):
    state = board.getFen()
    x = window.get_width()//4
    y = yStart
    for piece in range(len(state)):
        if state[piece].isnumeric():
            x += (int(state[piece])-1)*100
        if state[piece] == '/':     #goes to next row
            y += 103.5
            x = window.get_width()//4
            continue

        #displays black pieces
        if state[piece] == 'r':
            window.blit(scaleImage(RookB, pieceSize), (x,y))
        elif state[piece] == 'b':
            window.blit(scaleImage(BishopB, pieceSize), (x,y))
        elif state[piece] == 'n':
            window.blit(scaleImage(KnightB, pieceSize), (x,y))
        elif state[piece] == 'k':
            window.blit(scaleImage(KingB, pieceSize), (x,y))
        elif state[piece] == 'q':
            window.blit(scaleImage(QueenB, pieceSize), (x,y))
        elif state[piece] == 'p':
            window.blit(scaleImage(PawnB, pieceSize), (x,y))

        #displays white pieces
        elif state[piece] == 'R':
            window.blit(scaleImage(RookW, pieceSize), (x,y))
        elif state[piece] == 'B':
            window.blit(scaleImage(BishopW, pieceSize), (x,y))
        elif state[piece] == 'K':
            window.blit(scaleImage(KingW, pieceSize), (x,y))
        elif state[piece] == 'Q':
            window.blit(scaleImage(QueenW, pieceSize), (x,y))
        elif state[piece] == 'P':
            window.blit(scaleImage(PawnW, pieceSize), (x,y))
        elif state[piece] == 'N':
            window.blit(scaleImage(KnightW, pieceSize), (x,y))
        x += 100

#highlights currently clicked on square
def clicked_highlighted_square():
    if not move_list:
        return
    first = move_list[-1]
    xcord = window.get_width()/4
    ycord = yStart
    for letter in letters:
        if first[0] == letter:
            break
        xcord += 100

    for num in numbers:
        if first[1] == num:
            break
        ycord += 103.5

    if board.isOccupied(first[0] + first[1]):
        square2 = pg.Surface((100, 103), pg.SRCALPHA)
        square2.fill((255, 255, 0, 75))
        window.blit(square2, (xcord, ycord))
    elif board.isOccupied(first[0] + first[1]) == False and len(move_list)==1:
        move_list.clear()

    if len(move_list) == 2:
        if board.isLegalMove(move_list[-2] + move_list[-1]) and board.isOccupied(move_list[-1]):
            tempData = open("./Config/temp.dat", "w+b")
            tempData.write(board.board.fen().encode())
            tempData.close()
            import jake
        move(move_list[-2] + move_list[-1])
        
        move_list.clear()

#allows the choice to promote to specfic peices
def promotion_choice():
    square3 = pg.Surface((200,206.5))
    square3.fill((255, 255, 255, 75))
    window.blit(square3, (window.get_width()/4 - 225,window.get_height()/2))
    window.blit(scaleImage(QueenW, pieceSize),(window.get_width()/4 - 225, window.get_height()/2))
    window.blit(scaleImage(RookW, pieceSize), (window.get_width() / 4 - 125, window.get_height() / 2))
    window.blit(scaleImage(BishopW, pieceSize), (window.get_width() / 4 - 225, window.get_height() / 2 + 103.5))
    window.blit(scaleImage(KnightW,pieceSize), (window.get_width() / 4 - 125, window.get_height() / 2 + 103.5))

#Makes only valid moves for player
def move(uciMove):
    if board.isLegalMove(uciMove):
        board.pushMove(uciMove)

#runs the game
while True:
    window.fill(bg_color)
    window.blit(background, (window.get_width()/4,yStart))
    promotion_choice()
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
                    if clicked_pos[1] > 0 and clicked_pos[1] < yStart + (y * 103.5):
                        uciMove += numbers[y-1]
                        break


            move_list.append(uciMove)