import pygame
import shapes
import constants

pygame.init()

def main():
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
