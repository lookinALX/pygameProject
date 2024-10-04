import pygame
import shapes
import constants

pygame.init()


def main():
    # Ниже инициализация
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    rectangle1 = shapes.Rectangle((0, 0, 255), 50, 50, 150, 100, 0.1, 0.1)
    square1 = shapes.Square((255, 255, 0), 100, 100, 200, 0.1, 0.25)
    circle1 = shapes.Circle((255, 0, 0), 100, 100, 100, 0.1, 0.25)
    # Бесконечный цикл программы
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))

        # TODO: отрисовать и двигать круг, квадрат
        # Draw objects
        # rectangle1.draw(screen)
        square1.draw(screen)
        # Circle1.draw(screen)
        # Move objects
        # rectangle1.move()
        square1.move()
        # Circle1.move()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    print("Running")
    main()
