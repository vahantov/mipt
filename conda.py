import pygame as pg
import sys
import numpy as np
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
a = 238
b = 140
length = 180
width = 25
cos_45 = np.cos(np.pi/4)
x1 = [a, b]
x2 = [a + cos_45*length, b + cos_45*length]
x3 = [a + cos_45*(length + width), b + cos_45*(length - width)]
x4 = [a + cos_45*width, b - cos_45*width]


pg.draw.polygon(sc, BLACK, (x1, x2, x3, x4))

# right eye
pg.draw.circle(sc, BLACK, (A[0]+r/2, A[1]-r/5), r/6 + 2)
pg.draw.circle(sc, RED, (A[0]+r/2, A[1]-r/5), r/6)
pg.draw.circle(sc, BLACK, (A[0]+r/2, A[1]-r/5), r/14)


# right brov

a = 425
b = 250
length = 180
width = 28
cos_45 = np.cos(np.pi/4)
x1 = [a, b]
x2 = [a + cos_45*width, b + cos_45*width]
x3 = [a + cos_45*(length + width), b + cos_45*(width - length)]
x4 = [a + cos_45*length, b - cos_45*length]

pg.draw.polygon(sc, BLACK, (x1, x2, x3, x4))



pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.time.delay(1000)