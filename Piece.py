import chess
#AUTHOR -Isaac Goff
import pygame


screen = pygame.display.set_mode((1280, 720))

# In order in the dict value: Imagefile, speed, posx, posy, gravity, df, sur, health, attack
piece_stats = {"Wpawn": ["Images/Pieces/Pwned_White.png",20,100,475,0,-20,screen, 595,4],
               "Bpawn": ["Images/Pieces/Pwned_Black.png",20,1100,475,0,-20,screen, 685,-4],
                "Wrook": ["Images/Pieces/w_rook.png", 15, 100, 475, 2, -20, screen,595, 6],
               "Brook": ["Images/Pieces/CHiss.png", 15, 1100, 475, 2, -20, screen,685, -6],
               "Wknight": ["Images/Pieces/Horse_Girl_White.png", 25, 100, 475, -1, -20, screen,595, 5],
               "Bknight": ["Images/Pieces/Horse_Girl_Black.png", 25, 1100, 475, -1, -20, screen,685, -5],
               "Wbishop": ["Images/Pieces/w_bishop.png", 20, 100, 475, -2, -20, screen,595, 5],
               "Bbishop": ["Images/Pieces/BishopB.png", 20, 1100, 475, -2, -20, screen,685, -5],
               "Wqueen": ["Images/Pieces/w_queen.png", 25, 100, 475, -1, -20, screen,595, 7],
               "Bqueen": ["Images/Pieces/QueenB.png", 25, 1100, 475, -1, -20, screen,685, -7],
               "Wking": ["Images/Pieces/w_king.png", 10, 100, 475, 1, -20, screen,595, 6],
               "Bking": ["Images/Pieces/KingB.png", 10, 100, 475, 1, -20, screen,685, -6]}