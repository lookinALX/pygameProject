import pygame
import constants
from shapes import Circle


class Ball(Circle):
    def __init__(self, color, x, y, radius, speed_x=0, speed_y=0):
        super().__init__(color, x, y, radius, speed_x, speed_y)
        self.radius = radius
        self.center = [self.x, self.y]

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.center = [self.x, self.y]
        self.change_direction_if_out_of_window()

    def change_direction_if_out_of_window(self):
        self.center = [self.x, self.y]
        if self.x - self.radius <= 0 or self.x + self.radius >= constants.SCREEN_WIDTH:
            self.speed_x = -self.speed_x
            self.x += self.radius * 0.01 * self.speed_x / abs(self.speed_x)
        if self.y - self.radius <= 0 or self.y + self.radius >= constants.SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            self.y += self.radius * 0.01 * self.speed_y / abs(self.speed_y)

    def check_collision(self, other_rect):
        # Находим ближайшую точку от прямоугольника к мячу
        nearest_x = max(other_rect.x, min(self.x, other_rect.x + other_rect.width))
        nearest_y = max(other_rect.y, min(self.y, other_rect.y + other_rect.height))

        # Вычисляем расстояние от центра мяча до ближайшей точки
        distance_x = self.x - nearest_x
        distance_y = self.y - nearest_y

        # Если расстояние меньше радиуса, то есть коллизия
        if distance_x**2 + distance_y**2 <= self.radius**2:
            print('Collision')
            return True
        else:
            return False

    def change_direction_if_collision(self, other_rect):
        collision_detected = self.check_collision(other_rect)

        if collision_detected:
            # Определяем сторону столкновения
            overlap_left = abs(self.x + self.radius - other_rect.x)  # расстояние до левой границы
            overlap_right = abs(self.x - self.radius - (other_rect.x + other_rect.width))  # до правой границы
            overlap_top = abs(self.y + self.radius - other_rect.y)  # до верхней границы
            overlap_bottom = abs(self.y - self.radius - (other_rect.y + other_rect.height))  # до нижней границы

            if min(overlap_top, overlap_bottom) < min(overlap_left, overlap_right):
                # Вертикальное столкновение (удар сверху или снизу)
                self.speed_y = -self.speed_y
                if overlap_top < overlap_bottom:
                    self.y = other_rect.y - self.radius - 1  # Выносим мяч наверх
                else:
                    self.y = other_rect.y + other_rect.height + self.radius + 1  # Выносим мяч вниз
            else:
                # Горизонтальное столкновение (удар слева или справа)
                self.speed_x = -self.speed_x
                if overlap_left < overlap_right:
                    self.x = other_rect.x - self.radius - 1  # Выносим мяч влево
                else:
                    self.x = other_rect.x + other_rect.width + self.radius + 1  # Выносим мяч вправо





