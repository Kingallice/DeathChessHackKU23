import chess
#AUTHOR -Isaac Goff
import pygame


screen = pygame.display.set_mode((1280, 720))

# In order in the dict value: Imagefile, speed, posx, posy, gravity, df, sur, health, attack
piece_stats = {"Wpawn": ["Images/Pieces/pawnW.svg",20,0,475,0,-20,screen, 595,4] ,
               "Bpawn": ["Images/Pieces/pawnB.svg",20,100,475,0,-20,screen, 685,4],
                "Wrook": ["Images/Pieces/rookW.svg", 15, 0, 475, 2, -20, screen,595, 6],
               "Brook": ["Images/Pieces/rookB.svg", 15, 100, 475, 2, -20, screen,685, 6],
               "Wknight": ["Images/Pieces/knightW.svg", 25, 0, 475, -1, -20, screen,595, 5],
               "Bknight": ["Images/Pieces/knightB.svg", 25, 100, 475, -1, -20, screen,685, 5],
               "Wbishop": ["Images/Pieces/bishopW.svg", 20, 0, 475, -2, -20, screen,595, 5],
               "Bbishop": ["Images/Pieces/bishopB.svg", 20, 100, 475, -2, -20, screen,685, 5],
               "Wqueen": ["Images/Pieces/queenW.svg", 25, 0, 475, -1, -20, screen,595, 7],
               "Bqueen": ["Images/Pieces/queenB.svg", 25, 100, 475, -1, -20, screen,685, 7],
               "Wking": ["Images/Pieces/kingW.svg", 10, 0, 475, 1, -20, screen,595, 6],
               "Bking": ["Images/Pieces/kingB.svg", 10, 100, 475, 1, -20, screen,685, 6]}