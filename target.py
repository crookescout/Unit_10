# Scout Crooke, 12/13/19, this program performs unit 10 assignment option three: a target game

import pygame


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def draw_target(self):
        pygame.draw.circle(self.main_surface, (0, 0, 0), (250, 250), 200, 2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (250, 250), 160, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (250, 250), 120, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (250, 250), 80, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (250, 250), 40, 0)

    def get_Score(self, x, y):

