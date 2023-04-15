import pygame as pg
import sys
bg_color = (0,0,255) #blue
window = pg.display.set_mode()
pg.display.set_caption("DEATH CHESS")
pg.display.update()
pg.display.flip()
background = pg.image.load("board.png")

while True:
    for event in pg.event.get():  # PyGame event to quit the game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    window.fill(bg_color)
    window.blit(background, (window.get_width()/4,0))
    print( background.get_rect())
    pg.display.update()
    pg.display.flip()
