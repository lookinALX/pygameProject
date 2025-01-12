import pygame
import random
import math
import constants

pygame.init()










class bot():
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, speed_x=0, speed_y=0):
        super().__init__(x, y, speed_x, speed_y, color)
        self.width = width
        self.height = height
        self.dragging = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self , other_rect):
        self.x += self.speed_x
        self.y += self.speed_y


        if(other_rect.x <= 400):
        self.y = other_rect.y











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





























































