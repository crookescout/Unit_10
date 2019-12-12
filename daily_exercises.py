# Scout Crooke, 12/11/19, this program works on unit 10 daily exercises

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Pygame Demo - So Cool")
main_surface.fill((255, 255, 255))

pygame.draw.polygon(main_surface, (0, 255, 0), ((150, 25), (275, 100), (220, 275), (75, 275), (25, 100)), 0)
pygame.draw.rect(main_surface, (255, 0, 0), (200, 150, 100, 50), 0)
pygame.draw.circle(main_surface, (0, 0, 255), (300, 50), 18, 0)
pygame.draw.line(main_surface, (0, 0, 255), (60, 80), (120, 80), 3)
pygame.draw.line(main_surface, (0, 0, 255), (60, 140), (120, 80), 1)
pygame.draw.line(main_surface, (0, 0, 255), (60, 140), (120, 140), 3)
pygame.draw.ellipse(main_surface, (255, 10, 10), (250, 250, 40, 80), 1)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
