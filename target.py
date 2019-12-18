# Scout Crooke, 12/13/19, this program performs unit 10 assignment option three: a target game

import pygame


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def draw_target(self):
        x = int(self.main_surface.get_width()/2)
        y = int(self.main_surface.get_height()/2)

        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 200, 2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 160, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (x, y), 120, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (x, y), 80, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (x, y), 40, 0)

    def get_score(self, position):
        target_color = self.main_surface.get_at(position))


        self.main_surface.fill((255, 255, 255))
        self.draw_target()

        mouse_font = pygame.font.SysFont("Helvetica", 32)
        mouse_label = mouse_font.render(str(position), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))
