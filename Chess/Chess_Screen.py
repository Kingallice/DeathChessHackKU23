#Date: 4-14-23
#Author: Luke Slizoski
#This file is the gui for interactions with the board

import pygame as pg
import sys
import json
from Combat.jake import Jake
from Chess.chessManager import ChessManager
from GameGUI.ExitMenu import *

running = True

bg_color = (0,0,0) #black

letters = ['a','b','c','d','e','f','g','h']
numbers = ['8','7','6','5','4','3','2','1']
move_list = []
background = pg.image.load("Images/board.png")

pieceSize = (100, 100)
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

def openTempData():
    tempData = open("./Config/temp.dat", "r+b")
    tempDataText = tempData.read()
    tempData.close()
    return tempDataText

open("./Config/battle.dat", "w+").close()

def scaleImage(img, size):
    return pg.transform.smoothscale(img, size)

def getBattleData():
    battleFile = open("./Config/battle.dat", "r+")
    battleData = battleFile.read()
    if battleData:
        battleData = json.loads(battleData)
    else:
        return None
    battleFile.close()
    battleFile = open("./Config/battle.dat", "w+")
    battleFile.close()
    return battleData

class ChessBoard():
    def __init__(self) -> None:
        settings = json.loads(open("./Config/settings.dat", "r").read())
        tempData = open("./Config/temp.dat", "w+b")
        self.board = ChessManager()
        if len(openTempData()) > 0:
            self.board = ChessManager(openTempData().decode())

        self.window = pg.display.set_mode(settings["currResolution"])
        if settings["fullscreen"]:
            self.window = pg.display.set_mode((0,0), pg.FULLSCREEN)

        self.yStart = (self.window.get_height() - background.get_height())//2

    #highlights current square of mouse
    def highlight_square(self):
        pos = pg.mouse.get_pos()
        for x in range(self.window.get_width()//4,1160,100):
            increase = 0
            for y in range(self.yStart,self.yStart+828,103):
                increase += 0.5
                if pos[0] > x and pos[0] < x + 100:
                    if pos[1] > y and pos[1] < y + 103 + increase:
                        square = pg.Surface((100,103 + increase), pg.SRCALPHA)
                        square.fill((255,255,0,75))
                        self.window.blit(square,(x,y))

    def pawn_promo_highlight(self):
        pos = pg.mouse.get_pos()
        #trying to get pawn promotion square highlight
        for x in range(self.window.get_width()//4 - 255, self.window.get_width()//4 - 154, 100):
            for y in range(self.window.get_height()//2, self.window.get_height()//2 +104, 103):
                if pos[0] > x and pos[0] < x + 100:
                    if pos[1] > y and pos[1] < y + 103 + 0.5:
                        square = pg.Surface((100, 103 + 0.5), pg.SRCALPHA)
                        square.fill((255, 255, 0, 75))
                        self.window.blit(square, (x+28, y))

    #updates the pieces on the board
    def update_board(self, board):
        state = board.getFen()
        x = self.window.get_width()//4
        y = self.yStart
        for piece in range(len(state)):
            if state[piece].isnumeric():
                x += (int(state[piece])-1)*100
            if state[piece] == '/':     #goes to next row
                y += 103.5
                x = self.window.get_width()//4
                continue

            #displays black pieces
            if state[piece] == 'r':
                self.window.blit(scaleImage(RookB, pieceSize), (x,y))
            elif state[piece] == 'b':
                self.window.blit(scaleImage(BishopB, pieceSize), (x,y))
            elif state[piece] == 'n':
                self.window.blit(scaleImage(KnightB, pieceSize), (x,y))
            elif state[piece] == 'k':
                self.window.blit(scaleImage(KingB, pieceSize), (x,y))
            elif state[piece] == 'q':
                self.window.blit(scaleImage(QueenB, pieceSize), (x,y))
            elif state[piece] == 'p':
                self.window.blit(scaleImage(PawnB, pieceSize), (x,y))

            #displays white pieces
            elif state[piece] == 'R':
                self.window.blit(scaleImage(RookW, pieceSize), (x,y))
            elif state[piece] == 'B':
                self.window.blit(scaleImage(BishopW, pieceSize), (x,y))
            elif state[piece] == 'K':
                self.window.blit(scaleImage(KingW, pieceSize), (x,y))
            elif state[piece] == 'Q':
                self.window.blit(scaleImage(QueenW, pieceSize), (x,y))
            elif state[piece] == 'P':
                self.window.blit(scaleImage(PawnW, pieceSize), (x,y))
            elif state[piece] == 'N':
                self.window.blit(scaleImage(KnightW, pieceSize), (x,y))
            x += 100

    #highlights currently clicked on square
    def clicked_highlighted_square(self):
        if not move_list:
            return
        first = move_list[-1]
        xcord = self.window.get_width()/4
        ycord = self.yStart
        for letter in letters:
            if first[0] == letter:
                break
            xcord += 100

        for num in numbers:
            if first[1] == num:
                break
            ycord += 103.5

        if self.board.isOccupied(first[0] + first[1]):
            square2 = pg.Surface((100, 103), pg.SRCALPHA)
            square2.fill((255, 255, 0, 75))
            self.window.blit(square2, (xcord, ycord))
        elif self.board.isOccupied(first[0] + first[1]) == False and len(move_list)==1:
            move_list.clear()

        #Makes the move
        choice = ""
        if len(move_list) == 2:
            typeP = self.board.getPieceName(self.board.getPieceAt(move_list[0]))
            number = move_list[1]
            if typeP == 'pawn' and (number[1] == '8' or number[1] == '1'):
                choice = self.promotion_choice()
                move_list[-1] = move_list[-1] + choice


            if self.board.isLegalMove(move_list[-2] + move_list[-1]) and self.board.isOccupied(move_list[-1].replace(choice,"")):
                tempData = open("./Config/temp.dat", "w+b")
                tempData.write(self.board.board.fen().encode())
                tempData.close()
                conflict = {self.board.getColorAt(move_list[-2]): {"pos": move_list[-2], "piece": self.board.getColorAt(move_list[-2])[0].upper()+self.board.getPieceName(self.board.getPieceAt(move_list[-2]))},
                            self.board.getColorAt(move_list[-1]): {"pos": move_list[-1].replace(choice,""), "piece": self.board.getColorAt(move_list[-1])[0].upper()+self.board.getPieceName(self.board.getPieceAt(move_list[-1].replace(choice,"")))}, 
                            "attacker": self.board.getTurnColor(), "defender": self.board.getTurnColor(True)}
                tempData = open("./Config/battle.dat", "w+")
                json.dump(conflict,tempData)
                tempData.close()
                running = Jake().start()
                
            self.move(move_list[-2] + move_list[-1])
            
            move_list.clear()

    #allows the choice to promote to specfic peices
    def promotion_choice(self):
        while True:
            self.window.fill(bg_color)
            self.window.blit(background, (self.window.get_width() / 4, self.yStart))
            self.update_board(self.board)
            square3 = pg.Surface((200, 207))
            square3.fill((255, 255, 255, 75))
            self.window.blit(square3, (self.window.get_width() / 4 - 225, self.window.get_height() / 2))
            self.window.blit(scaleImage(QueenW, pieceSize), (self.window.get_width() / 4 - 225, self.window.get_height() / 2))
            self.window.blit(scaleImage(RookW, pieceSize), (self.window.get_width() / 4 - 125, self.window.get_height() / 2))
            self.window.blit(scaleImage(BishopW, pieceSize), (self.window.get_width() / 4 - 225, self.window.get_height() / 2 + 103.5))
            self.window.blit(scaleImage(KnightW, pieceSize), (self.window.get_width() / 4 - 125, self.window.get_height() / 2 + 103.5))
            self.pawn_promo_highlight()
            pg.display.update()
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP:  # event to get square/piece coordinates
                    pos = pg.mouse.get_pos()
                    if pos[0] > self.window.get_width()/4 - 255 and pos[0] < self.window.get_width()/4 - 155:
                        if pos[1] > self.window.get_height()/2 and pos[1] < self.window.get_height()/2 + 103.5:
                            return 'q'
                    if pos[0] > self.window.get_width()/4 - 155 and pos[0] < self.window.get_width()/4 - 55:
                        if pos[1] > self.window.get_height()/2 and pos[1] < self.window.get_height()/2 + 103.5:
                            return 'r'
                    if pos[0] > self.window.get_width()/4 - 255 and pos[0] < self.window.get_width()/4 - 155:
                        if pos[1] > self.window.get_height()/2 -103.5 and pos[1] < self.window.get_height()/2 + 207:
                            return 'b'
                    if pos[0] > self.window.get_width()/4 - 155 and pos[0] < self.window.get_width()/4 - 55:
                        if pos[1] > self.window.get_height()/2 and pos[1] < self.window.get_height()/2 + 207:
                            return 'n'

    #Makes only valid moves for player
    def move(self,uciMove):
        if self.board.isLegalMove(uciMove):
            self.board.pushMove(uciMove)

    #runs the game
    def start(self):
        isExitMenu = False
        menu = ExitMenu()
        running = True
        while running:
            self.window.fill(bg_color)
            self.window.blit(background, (self.window.get_width()/4,self.yStart))
            self.update_board(self.board)
            self.highlight_square()
            self.clicked_highlighted_square()
            if isExitMenu:
                menu.draw(window)
            pg.display.flip()

            temp = getBattleData()
            if temp:
                if "winner" in temp.keys():
                    if temp["winner"] == temp["attacker"]:
                        self.board.setPiece(temp[temp["defender"]]["pos"],
                                            self.board.getPieceChar(temp[temp["attacker"]]["piece"][1:]),
                                            self.board.getColor(temp["attacker"]))
                        self.board.removePiece(temp[temp["attacker"]]["pos"])
                    elif temp["winner"] == temp["defender"]:
                        self.board.setPiece(temp[temp["defender"]]["pos"],
                                            self.board.getPieceChar(temp[temp["defender"]]["piece"][1:]),
                                            self.board.getColor(temp["defender"]))
                        self.board.removePiece(temp[temp["attacker"]]["pos"])
                        #self.board.skipTurn()
                        

            for event in pg.event.get():  #event to quit the game
                if event.type == pg.QUIT:
                    running = False

                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        isExitMenu = True

                elif isExitMenu:
                    menu.draw(window)
                    bool = menu.handler(event)
                    if bool:
                        isExitMenu = False
                    elif bool == False:
                        running = False


                elif event.type == pg.MOUSEBUTTONUP: #event to get square/piece coordinates
                    clicked_pos = pg.mouse.get_pos()
                    uciMove = ''

                    #records the letter rank of clicked square
                    for x in range(1,9):
                        if clicked_pos[0] > self.window.get_width() / 4 and clicked_pos[0] < self.window.get_width() /4 + x * 100:
                            if clicked_pos[1] < 828 and clicked_pos[1] > 0:
                                uciMove += letters[x-1]
                                break

                    # records the number rank of clicked square
                    for y in range(1,9):
                        if clicked_pos[0] < self.window.get_width() / 4 + 800 and clicked_pos[0] > self.window.get_width() / 4:
                            if clicked_pos[1] > 0 and clicked_pos[1] < self.yStart + (y * 103.5):
                                uciMove += numbers[y-1]
                                break
                    move_list.append(uciMove)