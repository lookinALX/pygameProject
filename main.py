import pygame
import shapes
import constants

pygame.init()


def main():
    # Ниже инициализация
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    rectangle2 = shapes.Rectangle((255, 0, 255), 700, 200, 50, 150, 0, 0)
    gates1 = shapes.Rectangle((0, 128, 0), 0, 0, 10, 600,0,0  )
    gates2 = shapes.Rectangle((0, 128, 0), 790, 0, 10, 600, 0, 0)
    middle = shapes.Rectangle((0, 0, 255), 400, 0, 5, 600, 0, 0)
    circle1 = shapes.Circle(color=(255, 0, 0), x=400, y=350, radius=20, speed_x=0.3, speed_y=0.3)
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
        gates1.draw(screen)
        gates2.draw(screen)

        middle.draw(screen)

        rectangle2.drag()
        circle1.draw(screen)
        # Move objects
        circle1.move()
        circle1.change_direction_if_collision(rectangle2)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    print("Running")
    main()
