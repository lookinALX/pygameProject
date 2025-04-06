import pygame
import constants
import shapes

class Gate(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, ):
        super().__init__(color, x, y, width, height)

    # TODO: Написать функцию которая проверяет коллизию с мячом (только фронтально)

    def check_collision_with_ball(self, ball):
        # должна вернуть true если есть коллизия и false если нет
        if(ball.radius + ball.x  < self.x + 10):

            return True
        if (ball.radius + ball.x < self.x):

            return True

    score_bot = 0
    score_player = 0
    def score(self, ball):
        return self.check_collision_with_ball(ball) # ГОЛ если true















