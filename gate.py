#TODO: Создать класс Gate, который наследует прямоугольник. Создать конструктор (инит).
#TODO: Написать функцию которая проверяет коллизию с мячом

import pygame
import constants
import shapes
class Gate(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, ):
        super().__init__(color, x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    #def score(self, other_ball):
        #d_x = (other_ball.x - self.x)
        #if(self.x < constants.SCREEN_WIDTH/2):
         #   self.left = True
          #  if (self.left == True):

           #     print("голл игрока")
       # if (self.x > constants.SCREEN_WIDTH / 2):
        #    self.left = False
         #   if (self.left == False):

          #      print("голл бота")






        #if(self.x < d_x):
         #   left = False
          #  print("голл игрока")
        #if(self.x > d_x):
         #   right = False
          #  print("голл бота")

















