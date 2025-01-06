import pygame
import shapes
import constants

pygame.init()


def main():
    # Ниже инициализация
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    rectangle2 = shapes.Rectangle((255, 0, 255), 700, 200, 50, 150, 0, 0)
    # rectangle1 = shapes.Rectangle((0, 0, 255), 50, 50, 150, 100, 0.1, 0.1)
    # square1 = shapes.Square((255, 0, 0), 500, 300, 200, 0, 0)
    # square2 = shapes.Square((255, 255, 0), 100, 100, 20, 0.1, 0.05)
    circle1 = shapes.Circle(color=(255, 0, 0), x=100, y=400, radius=20, speed_x=0.08, speed_y=0.08)
    # Бесконечный цикл программы
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rectangle2.check_collision_with_mouse(pygame.mouse.get_pos()):
                    pygame.mouse.get_rel()
                    rectangle2.dragging = True
            if event.type == pygame.MOUSEBUTTONUP:
                rectangle2.dragging = False

        screen.fill((255, 255, 255))
        """Draw objects"""
        rectangle2.draw(screen)
        rectangle2.drag()
        # rectangle1.draw(screen)
        # square1.draw(screen)
        # square2.draw(screen)
        circle1.draw(screen)
        # Move objects
        # rectangle1.move()
        # rectangle1.check_collision(rectangle2)
        # square2.check_collision(rectangle2)
        # square2.move()
        circle1.move()
        #rectangle2.move()
        #circle1.check_collision(rectangle2)
        #circle1.change_direction()
        circle1.change_direction_if_collision(rectangle2)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    print("Running")
    main()
