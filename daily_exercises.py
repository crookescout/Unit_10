# Scout Crooke, 12/11/19, this program works on unit 10 daily exercises

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Pygame Demo - So Cool")
main_surface.fill((255, 255, 255))

pygame.draw.rect(main_surface, (255, 0, 0), (250, 200, 100, 50), 0)
pygame.draw.circle(main_surface, (0, 0, 255), (400, 100), 20, 0)
pygame.draw.polygon(main_surface, (0, 255, 0), ((100, 25), (200, 100), (150, 300), (50, 300), (25, 100)), 0)
pygame.draw.line(main_surface, (100, 100, 100), (200, 200), (45, 10), 3)
pygame.draw.ellipse(main_surface, (255, 10, 10), (300, 300, 20, 40), 1)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
