import pygame
import json
import os
from Chess.Chess_Screen import ChessBoard

btnYStart = 0
btnPadding = 10
btnWidth, btnHeight = 100, 20

pygame.init()

settings = {}
settings["fullscreen"] = True
settings["currResolution"] = (1280, 720)
settings["displayNum"] = 0

if not os.path.isdir("./Config"):
    os.mkdir("./Config")
if os.path.isfile("./Config/settings.dat"):
    settingsFile = open("./Config/settings.dat", 'r+')
else:
    settingsFile = open("./Config/settings.dat", 'w+')
settingsFileData = settingsFile.read()
if len(settingsFileData) > 0:
    settings = json.loads(settingsFileData)
    print("JSON", settings)
else:
    json.dump(settings, settingsFile)
settingsFile.close()

font = pygame.font.SysFont('Arial', 90)

screen = pygame.display.set_mode(settings["currResolution"])
if settings["fullscreen"]:
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

clock = pygame.time.Clock()
running = True
dt = 0

btnMenuText = ["Start", "Settings", "Exit"]
btnSettingsText = ["Fullscreen","Back"]
btnArr = []

titleText = pygame.font.Font('./Fonts/WereWolf.ttf', 300).render("Death Chess", True, "black")
settingsText = pygame.font.Font('./Fonts/WereWolf.ttf', 300).render("Settings", True, "black")
settingMenu = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif settingMenu and event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(btnArr)):
                btn = btnArr[i]
                mosPos = pygame.mouse.get_pos()
                if pygame.Rect(screen.get_rect().centerx - btn.get_rect().width/2, 
                            btnYStart - btn.get_rect().height/2 + i*(btn.get_rect().height + btnPadding), 
                            btn.get_rect().width,
                            btn.get_rect().height).collidepoint(mosPos[0], mosPos[1]):
                    if btnSettingsText[i] == "Display":
                        print(settings["displayNum"])
                        screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    elif btnSettingsText[i] == "Fullscreen":
                        settings["fullscreen"] = not pygame.display.is_fullscreen()
                        if settings["fullscreen"]:
                            screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode(settings["currResolution"])
                    elif btnSettingsText[i] == "Back":
                        settingMenu = False
                        settingsFile = open("./Config/settings.dat", 'w+')
                        json.dump(settings, settingsFile)
                        settingsFile.close()
                    break
        elif not settingMenu and event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(btnArr)):
                btn = btnArr[i]
                mosPos = pygame.mouse.get_pos()
                if pygame.Rect(screen.get_rect().centerx - btn.get_rect().width/2, 
                            btnYStart - btn.get_rect().height/2 + i*(btn.get_rect().height + btnPadding), 
                            btn.get_rect().width,
                            btn.get_rect().height).collidepoint(mosPos[0], mosPos[1]):
                    if btnMenuText[i] =="Start":
                            temp = open("./Config/temp.dat", "wb")
                            temp.close()
                            ChessBoard().start()
                    elif btnMenuText[i] == "Settings":
                            settingMenu = True
                    elif btnMenuText[i] == "Exit":
                            running = False
                    break

    screen.fill("white")

    if settingMenu:
        screen.blit(settingsText, (screen.get_rect().centerx - settingsText.get_width()/2, 10))

        btnArr = []
        btnYStart = settingsText.get_rect().height + btnPadding
        for i in range(len(btnSettingsText)):
            btnArr.append(font.render(btnSettingsText[i], True, "white", "black"))
            screen.blit(btnArr[i], (screen.get_rect().centerx - btnArr[i].get_rect().width/2, btnYStart - btnArr[i].get_rect().height/2 + i*(btnArr[i].get_rect().height + btnPadding)))

    else:
        screen.blit(titleText, (screen.get_rect().centerx - titleText.get_width()/2, 10))

        btnArr = []
        btnYStart = titleText.get_rect().height + btnPadding
        for i in range(len(btnMenuText)):
            btnArr.append(font.render(btnMenuText[i], True, "white", "black"))
            screen.blit(btnArr[i], (screen.get_rect().centerx - btnArr[i].get_rect().width/2, btnYStart - btnArr[i].get_rect().height/2 + i*(btnArr[i].get_rect().height + btnPadding)))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
