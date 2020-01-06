# Scout Crooke, 1/6/20, this program plays a target game

import target
import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Pygame Demo - So Cool")
main_surface.fill((255, 255, 255))

my_target = target.Target(main_surface)
my_target.draw_target()

num_clicks = 0
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and num_clicks < 5:
            num_clicks += 1
            my_target.get_score(pygame.mouse.get_pos())
