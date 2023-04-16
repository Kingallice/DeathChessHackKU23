import pygame as pg
pg.init()
window = pg.display.set_mode()

class ExitMenu:

    def __init__(self):
        self.width = 350
        self.height = 150
        self.menuBox = pg.Surface((self.width, self.height))
        self.menuBox.fill((152, 133, 88))
        self.yesBox = pg.Surface((100,50))
        self.yesBox.fill((144, 238, 144))
        self.noBox = pg.Surface((100, 50))
        self.noBox.fill((255,114,118))
        self.font = pg.font.SysFont('Arial', 50)
        self.yesText = self.font.render("Yes", True, (255,255,255))
        self.noText = self.font.render("No", True, (255,255,255))
        self.prompt = self.font.render("Quit?", True, (255,255,255))


    def draw(self, window):
        window.blit(self.menuBox,(window.get_width()/2 - self.width/2 +45, window.get_height()/2 -self.height/2))
        window.blit(self.prompt, (window.get_width()/2 - self.width/2 + 175, window.get_height()/2 -self.height/2 +20))
        window.blit(self.yesBox,(window.get_width()/2 - self.width/2 + 75, window.get_height()/2 -self.height/2 +70))
        window.blit(self.noBox, (window.get_width() / 2 - self.width/2 + 285, window.get_height() / 2 - self.height/2 + 70))
        window.blit(self.noText,((window.get_width() / 2 - self.width/2 + 305, window.get_height() / 2 - self.height/2 + 65)))
        window.blit(self.yesText,(window.get_width()/2 - self.width/2 + 85, window.get_height()/2 -self.height/2 +65))

    def handler(self,event):
        pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONUP:
            #Close exit menu (no)
            if pos[0] > window.get_width()/2 - self.width/2 + 285 and pos[0] < window.get_width()/2 - self.width/2 + 385:
                if pos[1] >  window.get_height()/2 -self.height/2 +70 and pos[1] <  window.get_height()/2 -self.height/2 +120:
                    return True
            #go to main menu (yes)
            if pos[0] > window.get_width()/2 - self.width/2 + 75 and pos[0] < window.get_width()/2 - self.width/2  + 175:
                if pos[1] >  window.get_height()/2 -self.height/2 +70 and pos[1] <  window.get_height()/2 -self.height/2 +120:
                    return False
