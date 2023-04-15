import pygame
import PlayerController
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

p1 = PlayerController.Player("Images/Pieces/CHiss.png",30,100,475,0,-20)
p2 = PlayerController.Player("Images/Pieces/Pwned.png",30,1100,475,0,-20)


p1_health = 595
p2_health = 685


timer_font = pygame.font.Font(None, 50) #None is the font of the text
screen.fill('White')

Meadow = pygame.image.load("Images/BackGround/Background.png").convert()




timer = timer_font.render('1:32', True, 'Green')
time_rect = timer.get_rect(center = (640,50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        p1.player_input()
        p2.player_input2()

        """if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and player_1_rect.bottom >= ground:
                player_gravity = -20

            if event.key == pygame.K_a:
                player_1_rect.x += -p1_movement

            if event.key == pygame.K_s:
                print("help")

            if event.key == pygame.K_d:
                player_1_rect.x += p1_movement"""


    screen.blit(Meadow,(0,0))   #layer 1. Draw most bottom layer first. The sky
                                    #layer 2. The ground

    #Draws the background of line
    pygame.draw.line(screen,"Cyan",(50,50), (600,50), width = 50)
    pygame.draw.line(screen, "Cyan", (680, 50), (1230, 50), width = 50)

    #Draws the actual Health Bar
    pygame.draw.line(screen, "Red", (55, 50), (p1_health, 50), width=40)
    pygame.draw.line(screen, "Red", (p2_health, 50), (1225, 50), width=40)



    if p1_health > 1 and p2_health < 1224:
        p1_health -= 1
        p2_health += 1



    screen.blit(timer,time_rect)



    p1.check_l_e()
    p2.check_l_e()


    p1.player_gravity()
    p2.player_gravity()

    screen.blit(p1.image,p1.rect)
    screen.blit(p2.image,p2.rect)


    #rect1.colliderrect(rect2) Checks for collision between two rectangles
    #rect1.colliderpoint((x,y)) Checks for a collision at one specific point













    pygame.display.update()
    clock.tick(60)

