import pygame
import PlayerController
from sys import exit
import Piece
import json

pygame.init()
settings = json.loads(open("./Config/settings.dat", "r").read())
Meadow = pygame.image.load("Images/BackGround/Background.png").convert()
timer_font = pygame.font.Font(None, 60)

test = 0
defTime = 92
overTime = 10
barSize = 500

class Jake():
    def __init__(self):
        self.screen = pygame.display.set_mode(settings["currResolution"])
        if settings["fullscreen"]:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.start_time = self.resetTime(defTime)
        battleInit = open("./Config/battle.dat", "r+")
        self.battleData = json.loads(battleInit.read())
        battleInit.close()
        self.env = (self.screen.get_rect().centery-Meadow.get_height()/2+600, 
                    self.screen.get_rect().centerx-Meadow.get_width()/2, 
                    self.screen.get_rect().centerx+Meadow.get_width()/2)
        self.p1 = self.get_piece_stats(self.battleData, "attacker")
        self.p2 = self.get_piece_stats(self.battleData, "defender")
    def resetTime(self,nexttime):
        return pygame.time.get_ticks()//1000 + nexttime
    
    def get_time(self):
        return self.start_time - pygame.time.get_ticks()//1000

    def display_time(self):
        left, right = str(self.get_time()//60).split(".")[0], ("0"+str(self.get_time()%60))
        return left +":"+ right[-2:]

    # Created function that pulls piece stat list from piece.py dict, and splits it before returning stats
    def get_piece_stats(self, data, side):
        pieceList = Piece.piece_stats[data[side]["piece"]]
        color = data[side]["piece"][0]
        location = data[side]["pos"]
        image = pieceList[0]
        speed = pieceList[1]
        posx= pieceList[2]
        posy=pieceList[3]
        gravity=pieceList[4]
        df=pieceList[5]
        sur=pieceList[6]
        health=pieceList[7]
        attack =pieceList[8]

        return PlayerController.Player(side, color, location, image, speed, posx, posy, gravity, df, sur, health, attack, self.env)
    
    def start(self):
        running = True
        while running:
            self.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.get_time() <= 0:
                if (self.p1.health/self.p1.max_health) > (self.p2.health/self.p2.max_health):
                    running = not self.p1.win()
                elif (self.p1.health/self.p1.max_health) < (self.p2.health/self.p2.max_health):
                    running = not self.p2.win()
                else:
                    self.start_time = self.resetTime(overTime)
                    

            infoHeight = self.screen.get_rect().centery-Meadow.get_height()/2 + 30

            timer = timer_font.render(str(self.display_time()), True, 'Green')
            time_rect = timer.get_rect(center=(self.screen.get_rect().centerx, infoHeight))

            self.screen.blit(Meadow,(self.screen.get_width()/2 - Meadow.get_width()/2,self.screen.get_height()/2 - Meadow.get_height()/2))   #layer 1. Draw most bottom layer first. The sky
                                            #layer 2. The ground
            #Draws the background of line
            pygame.draw.line(self.screen,"Cyan",(self.env[1]+10,infoHeight), (self.env[1]+barSize+20,infoHeight), width = 50)
            pygame.draw.line(self.screen, "Cyan", (self.env[2]-barSize-20, infoHeight), (self.env[2]-10,infoHeight), width = 50)

            #Draws the actual Health Bar
            pygame.draw.line(self.screen, "Red", (self.env[1]+15, infoHeight), (self.env[1]+15 + (max(0,self.p1.health/self.p1.max_health)*barSize), infoHeight), width=40)
            pygame.draw.line(self.screen, "Red", (self.env[2]-15 - (max(0,self.p2.health/self.p2.max_health)*barSize), infoHeight), (self.env[2]-15 , infoHeight), width=40)

            self.screen.blit(timer,time_rect)

            self.p1.player_input(self.p2)
            self.p2.player_input2(self.p1)

            if self.p1.health <= 0:
                running = not self.p1.win()
            elif self.p2.health <= 0:
                running = not self.p2.win()

            self.p1.check_l_e()
            self.p2.check_l_e()

            self.p1.player_gravity()
            self.p2.player_gravity()

            self.screen.blit(self.p1.image,self.p1.rect)
            self.screen.blit(self.p2.image,self.p2.rect)

            #rect1.colliderrect(rect2) Checks for collision between two rectangles
            #rect1.colliderpoint((x,y)) Checks for a collision at one specific point

            pygame.display.update()
            self.clock.tick(60)