import pygame as pg
import cells as c
import random as rd

pg.init()
case = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def drowcircle(centerc, sur):
    pg.draw.circle(sur, (255, 0, 0), centerc, 60, 0)
    pg.draw.circle(sur, (255, 255, 255), centerc, 55, 0)


def risovakamf(key, sur):
    center = (-110, -110)
    if key == pg.K_KP7:
        center = (83, 83)
    if key == pg.K_KP8:
        center = (249, 83)
    if key == pg.K_KP9:
        center = (415, 83)
    if key == pg.K_KP4:
        center = (83, 249)
    if key == pg.K_KP5:
        center = (249, 249)
    if key == pg.K_KP6:
        center = (415, 249)
    if key == pg.K_KP1:
        center = (83, 415)
    if key == pg.K_KP2:
        center = (249, 415)
    if key == pg.K_KP3:
        center = (415, 415)

    drowcircle(center, sur)

    return center


def cellstatus(pos):
    if pos == (83, 83):
        c.cell1 = False
    if pos == (249, 83):
        c.cell2 = False
    if pos == (415, 83):
        c.cell3 = False
    if pos == (83, 249):
        c.cell4 = False
    if pos == (249, 249):
        c.cell5 = False
    if pos == (415, 249):
        c.cell6 = False
    if pos == (83, 415):
        c.cell7 = False
    if pos == (249, 415):
        c.cell8 = False
    if pos == (415, 415):
        c.cell9 = False


def crossdraw(sur):
    peremka = 1
    if peremka == 1:
        if c.cell1 != False:
            pg.draw.line(sur, (0, 0, 255), (23, 143), (143, 23), 5)
            pg.draw.line(sur, (0, 0, 255), (23, 23), (143, 143), 5)
        else:
            peremka += 1
    if peremka == 2:
        if c.cell2 != False:
            pg.draw.line(sur, (0, 0, 255), (189, 143), (309, 23), 5)
            pg.draw.line(sur, (0, 0, 255), (189, 23), (309, 143), 5)


if __name__ == "__main__":
    key = None
    screen = pg.display.set_mode([500, 500])
    pg.display.set_caption('x&o')

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                key = event.key

        screen.fill((255, 255, 255))

        cellstatus(risovakamf(key, screen))
        crossdraw(screen)

        r1 = pg.Rect((0, 166), (500, 4))
        r2 = pg.Rect((0, 332), (500, 4))
        r3 = pg.Rect((166, 0), (4, 500))
        r4 = pg.Rect((332, 0), (4, 500))

        pg.draw.rect(screen, (0, 0, 0), r1)
        pg.draw.rect(screen, (0, 0, 0), r2)
        pg.draw.rect(screen, (0, 0, 0), r3)
        pg.draw.rect(screen, (0, 0, 0), r4)

        # pg.draw.line(screen, (0,0,255), (23, 143), (143, 23), 5)
        # pg.draw.line(screen, (0,0,255), (23, 23), (143, 143), 5)

        pg.display.flip()

    pg.quit()
