import pygame
import constants
import shapes


class Bot(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, speed_x=0, speed_y=0):
        super().__init__(color, x, y, width, height, speed_x, speed_y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))


    def follow_ball(self, ball: shapes.Circle):
        y_where_ball_comes = 0
        half_field = constants.SCREEN_WIDTH / 2
        is_crossed_half_field = True if ball.x >= half_field else False

        #TODO: Посчитать правильно y_where_ball_comes через время и скорости
        if not is_crossed_half_field:
            distance_between_ball_and_bot = ball.x - self.x - self.width
            y_where_ball_comes = ???

        if (self.y + self.height / 2 < y_where_ball_comes) and (not is_crossed_half_field):
            self.y += self.speed_y
            print(f"bot y --> {self.y} ; y where ball comes --> {y_where_ball_comes}")
        elif (self.y + self.height / 2 > y_where_ball_comes) and (not is_crossed_half_field):
            self.y -= self.speed_y
            print(f"bot y --> {self.y} ; y where ball comes --> {y_where_ball_comes}")
        else:
            self.y = self.y
            print(f"bot y --> {self.y} ; y where ball comes --> {y_where_ball_comes}")
