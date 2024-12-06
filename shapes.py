"""
Этот модуль реализует основные геометрические фигуры, такие как прямоугольник, квадрат, тругольник и круг.
"""

import pygame
import random
import math
import constants

pygame.init()  # Запускаем движок


class Shape:
    """
    Базовый класс для всех фигур.

    Атрибуты:
    color : tuple
        Цвет фигуры в формате (R, G, B).
    x : float
        Координата х
    y : float
        Координата y
    Методы:
    draw(self, surface):
        рисует  на поверхности
        surface - поверхность для отрисовки объекта
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        скорость по обоим ординатам
    def rotate(self, angle):
          поворот фигуры по чесовой стрелке
    """

    def __init__(self, x: float, y: float, speed_x: float, speed_y: float, color=(255, 255, 255)):
        self.color = color
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self, surface):
        pass

    def move(self):
        pass

    def rotate(self, surface, angle):
        pass


class Rectangle(Shape):
    """
                Класс определяющий прямоугольник.

        Атрибуты:
        color : tuple
            Цвет фигуры в формате (R, G, B).
        #: дописать документ строчку
        x : double
            Координата по оси Х левого верхнего угла прямоугольника
        Методы:
        draw(self, surface):
            рисует объект на поверхности
            surface - поверхность для отрисовки объекта
            def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        скорость по обоим ординатам
                if self.x <= 0 or self.x + self.width >= constants.SCREEN_WIDTH:
            self.speed_x = -self.speed_x

        if self.y <= 0 or self.y + self.height >= constants.SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            если прямоугольник приближается к конця какой либо стороны окна то он отцкакивает

            def rotate(self, surface, angle):
        pygame.transform.rotate(surface, -angle)
             поворот фигуры по чесовой стрелке
        """

    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, speed_x=0, speed_y=0):
        super().__init__(x, y, speed_x, speed_y, color)
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x + self.width >= constants.SCREEN_WIDTH:
            self.speed_x = -self.speed_x

        if self.y <= 0 or self.y + self.height >= constants.SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def rotate(self, surface, angle):
        pygame.transform.rotate(surface, -angle)

    def check_collision(self, other_rect):
      collision_detected = False
      if (self.x + self.width >= other_rect.x and self.y + self.height >= other_rect.y) and (
            other_rect.y + other_rect.height >= self.y and other_rect.x + other_rect.width >= self.x):
        collision_detected = True
        print("COLLISION!")
      else:
        collision_detected = False
      return collision_detected







class Square(Rectangle):
    """
     Класс определяющий квадрат

        Атрибуты:
        color : tuple
            Цвет фигуры в формате (R, G, B).
        #: дописать документ строчку
        x : double
            Координата по оси Х левого верхнего угла квадрата
        Методы:
        draw(self, surface):
            рисует объект на поверхности
            surface - поверхность для отрисовки объекта
            def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
           скорость по обоим ординатам


        def rotate(self, angle):
             поворот фигуры по чесой стрелке
    """

    def __init__(self, color, x, y, size, speed_x=0, speed_y=0):
        super().__init__(color, x, y, size, size, speed_x, speed_y)
        self.size = size
        self.size = size

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.size > constants.SCREEN_WIDTH or self.x < 0:
            self.speed_x = -self.speed_x

        if self.y + self.size > constants.SCREEN_HEIGHT or self.y < 0:
            self.speed_y = -self.speed_y

    def rotate(self, surface, angle):
        pygame.transform.rotate(surface, -angle)

    def check_collision(self, other_rect):
        """
        Проверка коллизии с другим объектом.

        Parameters:
            other_rect (class Square): Прямоугольник другого объекта

        Returns:
            bool: True, если объекты пересекаются, иначе False
        """
        collision_detected = False
        if (self.x + self.size >= other_rect.x and self.y + self.size >= other_rect.y) and (
                other_rect.y + other_rect.size >= self.y and other_rect.x + other_rect.size >= self.x):
            collision_detected = True
            print("COLLISION!")
        else:
            collision_detected = False
        return collision_detected

class Circle(Shape):
    """
         Класс определяющий круга.

        Атрибуты:
        color : tuple
            Цвет фигуры в формате (R, G, B).
        #: дописать документ строчку
        x : double
            Координата по оси Х левого верхнего угла круга и его радиус
        Методы:
        draw(self, surface):
            рисует объект на поверхности
            surface - поверхность для отрисовки объекта

            def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
           скорость по обоим ординатам


        def rotate(self, angle):
             поворот фигуры по чесой стрелке
    """

    def __init__(self, color, x, y, radius, speed_x=0, speed_y=0):
        super().__init__(color=color, x=x, y=y, speed_x=speed_x, speed_y=speed_y)
        self.radius = radius
        self.center = [self.x, self.y]

    def draw(self, surface):
        pygame.draw.circle(surface, color=self.color, center=tuple(self.center), radius=self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.center = [self.x, self.y]

        if(self.x- self.radius <= 0 or self.x + self.radius >= constants.SCREEN_WIDTH ):
            self.speed_x = -self.speed_x

        if (self.y - self.radius <= 0 or self.y + self.radius >= constants.SCREEN_HEIGHT):
            self.speed_y = -self.speed_y

    #def check_collision(self, other_circle):







