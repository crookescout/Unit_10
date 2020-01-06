# Scout Crooke, 1/6/20, this program performs unit 10 assignment option 3: a target game

import pygame


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.score = 0

    def draw_target(self):
        """
        this method draws 6 different colored circles with different sizes to form a target
        :return: none
        """
        x = int(self.main_surface.get_width()/2)
        y = int(self.main_surface.get_height()/2)
        pygame.draw.circle(self.main_surface, (255, 255, 254), (x, y), 200, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 200, 2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 160, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (x, y), 120, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (x, y), 80, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (x, y), 40, 0)

    def get_score(self, position):
        """
        this method calculates the user's score depending on what color circle of the target they click on
        :param position: the position is the mouse coordinates on the target
        :return: none
        """
        target_color = self.main_surface.get_at(position)
        if target_color == (255, 255, 0, 255):
            self.update_score(9)
        elif target_color == (255, 0, 0, 255):
            self.update_score(7)
        elif target_color == (0, 0, 255, 255):
            self.update_score(5)
        elif target_color == (0, 0, 0, 255):
            self.update_score(3)
        elif target_color == (255, 255, 254, 255):
            self.update_score(1)

    def update_score(self, score):
        """
        this method updates the user's score and displays it on the screen
        :param score: the user's score depending on the color of the circle they clicked on the target
        :return: none
        """
        self.main_surface.fill((255, 255, 255))
        self.draw_target()
        self.score += score
        mouse_font = pygame.font.SysFont("Helvetica", 32)
        mouse_label = mouse_font.render(str(self.score), 1, (0, 0, 0))
        self.main_surface.blit(mouse_label, (30, 30))

