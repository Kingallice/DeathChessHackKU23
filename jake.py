import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50) #None is the font of the text

screen.fill('White')

background = pygame.image.load("Images/BackGround/Background.png").convert()
rook = pygame.image.load("Images/Pieces/CHiss.png").convert_alpha()

player_1_x = 100

text_surface = test_font.render('0', True, 'Green')

player_surface = pygame.image.load("Images/Pieces/Chiss.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))   #layer 1. Draw most bottom layer first. The sky
                                    #layer 2. The ground
    screen.blit(text_surface,(640,50))

    screen.blit(rook,(player_1_x,475))






    pygame.display.update()
    clock.tick(60)

