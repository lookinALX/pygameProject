import pygame
import constants
import shapes

class Gate(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, ):
        super().__init__(color, x, y, width, height)

        self.side = "left" if x == 0 else "right"

    def check_collision_with_ball(self, ball):
        # должна вернуть true если есть коллизия и false если нет
        if self.side == "left":
            if(ball.x - ball.radius < self.x + self.width):
                return True
        else:
            if (ball.radius + ball.x > self.x):
                return True

    score_bot = 0
    score_player = 0
    def score(self, ball):
        if self.check_collision_with_ball(ball):
            return True