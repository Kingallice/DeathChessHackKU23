import pygame as pg
import sys
bg_color = (0,0,255) #blue
window = pg.display.set_mode()
pg.display.set_caption("DEATH CHESS")
pg.display.update()
pg.display.flip()
background = pg.image.load("board.png")

#Checks to see if mouse is on certain squares
def highlight_square(pos):
    for x in range(360,1160,100):
        increase = 0
        for y in range(0,828,103):
            increase += 0.5
            if pos[0] > x and pos[0] < x + 100:
                if pos[1] > y and pos[1] < y + 103 + increase:
                    square = pg.Surface((100,103 + increase), pg.SRCALPHA)
                    square.fill((255,255,0,75))
                    window.blit(square,(x,y))

while True:
    pos = pg.mouse.get_pos()
    window.fill(bg_color)
    window.blit(background, (window.get_width()/4,0))
    highlight_square(pos)
    pg.display.update()
    pg.display.flip()

    for event in pg.event.get():  #event to quit the game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONUP: #event to get square/piece coordinates
            clicked_pos = pos
            print(pos)



