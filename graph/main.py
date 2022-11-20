import pygame as pg
import random as rd

pg.init()
pg.display.set_caption('graphs')
size = [800, 600]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

def getposX():
    x = rd.randint(0, 800)
    return x
def getposY():
    y = rd.randint(0,600)
    return y



if __name__ == '__main__':
    running = True
    x = rd.randint(0, 700)
    y = rd.randint(0, 500)
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((255, 255, 255))

        pg.draw.circle(screen, (255, 15, 0), (x, y), 30, 0)

        pg.display.flip()
        clock.tick(30)

    pg.quit()
