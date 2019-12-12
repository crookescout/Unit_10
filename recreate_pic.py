# Scout Crooke, 12/11/19, this program recreates the picture of the city at night

import pygame, sys
from pygame.locals import *
import random

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Pygame Demo - So Cool")
main_surface.fill((16, 78, 139))


def make_star():
    x = random.randint(1, 500)
    y = random.randint(1, 400)
    pygame.draw.circle(main_surface, (184, 184, 184), (x, y), 2, 0)


for x in range(20):
    make_star()


def make_rect(a, b, c, d):
    pygame.draw.rect(main_surface, (0, 0, 0), (a, b, c, d), 0)


def make_window(e, f):
    pygame.draw.rect(main_surface, (255, 255, 0), (e, f, 10, 10), 0)


make_rect(0, 250, 30, 200)
make_rect(30, 180, 80, 250)
make_rect(110, 290, 70, 200)
make_rect(180, 250, 70, 200)
make_rect(245, 160, 80, 250)
make_rect(315, 320, 50, 100)
make_rect(365, 290, 60, 200)
make_rect(425, 160, 60, 300)
make_rect(480, 220, 60, 250)

pygame.draw.circle(main_surface, (184, 184, 184), (50, 75), 30, 0)
pygame.draw.ellipse(main_surface, (110, 110, 110), (136, 180, 250, 550), 20)

make_window(45, 220)
make_window(80, 240)
make_window(45, 300)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
