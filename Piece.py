import chess
#AUTHOR -Isaac Goff
import pygame


screen = pygame.display.set_mode((1280, 720))

# In order in the dict value: Imagefile, speed, posx, posy, gravity, df, sur
piece_stats = {"Wpawn": ["Images/Pieces/Pwned_White.png",20,100,475,0,-20,screen],
               "Bpawn": ["Images/Pieces/Pwned_Black.png",20,1100,475,0,-20,screen],
                "Wrook":["Images/Pieces/w_rook.png", 15, 100, 475, 2, -20, screen],
               "Brook": ["Images/Pieces/CHiss.png", 15, 1100, 475, 2, -20, screen],
               "Wknight": ["Images/Pieces/Horse_Girl_White.png", 25, 100, 475, -1, -20, screen],
               "Bknight": ["Images/Pieces/Horse_Girl_Black.png", 25, 1100, 475, -1, -20, screen],
               "Wbishop": ["Images/Pieces/w_bishop.png", 20, 100, 475, -2, -20, screen],
               "Bbishop": ["Images/Pieces/BishopB.png", 20, 1100, 475, -2, -20, screen],
               "Wqueen": ["Images/Pieces/w_queen.png", 25, 100, 475, -1, -20, screen],
               "Bqueen": ["Images/Pieces/QueenB.png", 25, 1100, 475, -1, -20, screen],
               "Wking": ["Images/Pieces/w_king.png", 10, 100, 475, 1, -20, screen],
               "Bking": ["Images/Pieces/KingB.png", 10, 100, 475, 1, -20, screen]}