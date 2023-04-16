import pygame
import PlayerController
from sys import exit
import Piece
import json
import re
import time

settings = json.loads(open("./Config/settings.dat", "r").read())

test = 0
defTime = 72
start_time = time.time() + defTime
barSize = 500

def resetTime():
    start_time = defTime + time.time()

def display_time():
    current_time = start_time - time.time()
    
 #   if timeright < 100:
  #      timeright = "0"+str(timeright)
   # elif not timeright:
    #    timeright = "00000"
    #timeStr = (str(timeleft) + ":" + str(timeright)+"000")
    #timeObj = re.search("[0-9]:[0-5][0-9]", timeStr)
    #if timeObj:
    return re.search("[0-9][0-9]:[0-5][0-9]", str(current_time))#timeObj[0][0:4]


def get_time():
    time_left = start_time - time.time()
    return time_left

pygame.init()
screen = pygame.display.set_mode(settings["currResolution"])
if settings["fullscreen"]:
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

piece1 = "Wpawn"
piece2 = 'Bqueen'
conflict = {"location": "a2", "defender":"Wpawn", "attacker":"BQueen"}

Meadow = pygame.image.load("Images/BackGround/Background.png").convert()

env = (screen.get_rect().centery-Meadow.get_height()/2+600, 
       screen.get_rect().centerx-Meadow.get_width()/2, 
       screen.get_rect().centerx+Meadow.get_width()/2)

# Created function that pulls piece stat list from piece.py dict, and splits it before returning stats
def get_piece_stats(piece1):
    color = piece1[0]
    type = piece1[1:]
    pieceList = Piece.piece_stats[piece1]
    image = pieceList[0]
    speed = pieceList[1]
    posx= pieceList[2]
    posy=pieceList[3]
    gravity=pieceList[4]
    df=pieceList[5]
    sur=pieceList[6]
    health=pieceList[7]
    attack =pieceList[8]

    return PlayerController.Player(image, speed, posx, posy, gravity, df, sur, health, attack, env)

p1 = get_piece_stats(piece1)

p2 = get_piece_stats(piece2)



timer_font = pygame.font.Font(None, 60) #None is the font of the text

running = True

while running:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if get_time() <= 0:
            if p1.health > p2.health:
                running = not p1.win()
            elif p1.health < p2.health:
                running = not p2.win()
            else:
                resetTime()
            

    infoHeight = screen.get_rect().centery-Meadow.get_height()/2 + 30

    timer = timer_font.render(str(display_time()), True, 'Green')
    time_rect = timer.get_rect(center=(screen.get_rect().centerx, infoHeight))

    screen.blit(Meadow,(screen.get_width()/2 - Meadow.get_width()/2,screen.get_height()/2 - Meadow.get_height()/2))   #layer 1. Draw most bottom layer first. The sky
                                    #layer 2. The ground
    #Draws the background of line
    pygame.draw.line(screen,"Cyan",(env[1]+10,infoHeight), (env[1]+barSize+20,infoHeight), width = 50)
    pygame.draw.line(screen, "Cyan", (env[2]-barSize-20, infoHeight), (env[2]-10,infoHeight), width = 50)

    #Draws the actual Health Bar
    pygame.draw.line(screen, "Red", (env[1]+15, infoHeight), (env[1]+15 + (max(0,p1.health/p1.max_health)*barSize), infoHeight), width=40)
    pygame.draw.line(screen, "Red", (env[2]-15 - (max(0,p2.health/p2.max_health)*barSize), infoHeight), (env[2]-15 , infoHeight), width=40)

    screen.blit(timer,time_rect)

    p1.player_input(p2)
    p2.player_input2(p1)

    if p1.health <= 0:
        running = not p1.win()
    elif p2.health <= 0:
        running = not p2.win()

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

pygame.quit()