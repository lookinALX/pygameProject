import pygame
import constants
import shapes


class Bot(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, speed_x=0, speed_y=0):
        super().__init__(color, x, y, width, height, speed_x, speed_y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    #TODO: Napisat'
    def move(self, ball):
        pass

    # TODO: Perepisat'
    def check_collision(self, other_rect):
        pass
