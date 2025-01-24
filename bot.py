import pygame
import constants
import shapes


class Bot(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, speed_x=0, speed_y=0):
        super().__init__(color, x, y, width, height, speed_x, speed_y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def follow_ball(self, ball: shapes.Circle):
        a = 0
        half_field = constants.SCREEN_WIDTH / 2
        is_crossed_half_field = True if ball.x >= half_field else False

        if not is_crossed_half_field:
            d = ball.x - self.x - self.width
            ctan_phi = ball.speed_y / ball.speed_x
            a = d * ctan_phi + ball.y

        if (self.y + self.width / 2 <= a) and (not is_crossed_half_field):
            self.y += self.speed_y
        elif (self.y + self.width / 2 >= a) and (not is_crossed_half_field):
            self.y -= self.speed_y
        else:
            self.y = self.y
