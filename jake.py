import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

p1_health = 595
p2_health = 685

timer_font = pygame.font.Font(None, 50) #None is the font of the text
screen.fill('White')

background = pygame.image.load("Images/BackGround/Background.png").convert()
rook = pygame.image.load("Images/Pieces/CHiss.png").convert_alpha()



timer = timer_font.render('1:32', True, 'Green')
time_rect = timer.get_rect(center = (640,50))


player_1_surface = pygame.image.load("Images/Pieces/Chiss.png").convert_alpha()
player_1_rect = player_1_surface.get_rect(topleft = (100,475))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))   #layer 1. Draw most bottom layer first. The sky
                                    #layer 2. The ground


    #Draws the background of line
    pygame.draw.line(screen,"Cyan",(50,50), (600,50), width = 50)
    pygame.draw.line(screen, "Cyan", (680, 50), (1230, 50), width = 50)

    #Draws the actual Health Bar
    pygame.draw.line(screen, "Red", (55, 50), (p1_health, 50), width=40)
    pygame.draw.line(screen, "Red", (p2_health, 50), (1225, 50), width=40)

    p1_health -= 1
    p2_health += 1

    #pygame.draw.line(screen,"White",(100,50))



    screen.blit(timer,time_rect)

    screen.blit(player_1_surface,player_1_rect)


    #rect1.colliderrect(rect2) Checks for collision between two rectangles
    #rect1.colliderpoint((x,y)) Checks for a collision at one specific point



    pygame.display.update()
    clock.tick(60)

