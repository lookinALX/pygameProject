import pygame
import constants
import shapes


class Player(shapes.Rectangle):
    def __init__(self, color: tuple, x: float, y: float, width: float, height: float, speed_x=0, speed_y=0):
        super().__init__(color, x, y, width, height, speed_x, speed_y)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def check_collision_with_mouse(self, mouse_position):
        collision_detected = False
        if mouse_position is not None:
            if (self.y < mouse_position[1] < self.y + self.height) and (
                    self.x < mouse_position[0] < self.x + self.width):
                collision_detected = True
                print("COLLISION!")
        return collision_detected

    def drag(self):
        if self.dragging:
            delta_pos = pygame.mouse.get_rel()
            self.speed_y = delta_pos[1]
            self.move()