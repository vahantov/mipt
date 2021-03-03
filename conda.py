import pygame as pg
import sys

# Константы цветов

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
RED = (255, 0, 0)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

# Инициализация дисплея

sc = pg.display.set_mode((800, 600))

# координаты для рисования

r = 200
A = (400, 300)

rect = pg.Rect((A[0] - r/2, A[1] + r / 2, r, r/5))

# здесь будут рисоваться фигуры

# big yellow
pg.draw.circle(sc, WHITE, A, r+1000)
pg.draw.circle(sc, BLACK, A, r+2)
pg.draw.circle(sc, YELLOW, A, r)

# smile
pg.draw.rect(sc, BLACK, rect)

# left eye
pg.draw.circle(sc, BLACK, (A[0]-r/2, A[1]-r/5), r/5 + 2)
pg.draw.circle(sc, RED, (A[0]-r/2, A[1]-r/5), r/5)
pg.draw.circle(sc, BLACK, (A[0]-r/2, A[1]-r/5), r/12)

# left brov
pg.draw.polygon(sc, PINK,
                    [[20, 60], [70, 30],
                     [50, 10], [0, 40]])

# right eye
pg.draw.circle(sc, BLACK, (A[0]+r/2, A[1]-r/5), r/6 + 2)
pg.draw.circle(sc, RED, (A[0]+r/2, A[1]-r/5), r/6)
pg.draw.circle(sc, BLACK, (A[0]+r/2, A[1]-r/5), r/14)


pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)