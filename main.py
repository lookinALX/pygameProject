import pygame
import shapes
import constants

pygame.init()


def main():
    # Ниже инициализация
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    #rectangle1 = shapes.Rectangle((0, 0, 255), 50, 50, 150, 100, 0.1, 0.1)
    #square1 = shapes.Square((255, 255, 0), 100, 100, 200, 0.1, 0.25)
    circle1 = shapes.Circle(color=(255, 0, 0), x=100, y=100, radius=20, speed_x=0.1, speed_y=0.1)
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
        #square1.draw(screen)
        circle1.draw(screen)
        # Move objects
        # rectangle1.move()
        # square1.move()
        circle1.move()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    print("Running")
    main()
