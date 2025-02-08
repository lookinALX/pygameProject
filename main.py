import pygame
import shapes
import constants
import bot
import ball
import player

pygame.init()


def main():
    # Ниже инициализация
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    gates1 = shapes.Rectangle((0, 128, 0), 0, 0, 10, 600,0,0  )
    gates2 = shapes.Rectangle((0, 128, 0), 790, 0, 10, 600, 0, 0)
    middle = shapes.Rectangle((0, 0, 255), 400, 0, 5, 600, 0, 0)
    game_ball = ball.Ball(color=(255, 0, 0), x=720, y=50, radius=20, speed_x=0.05, speed_y=0.05)
    main_player = player.Player((255, 0, 255),700, 200, 50, 150, 0, 0)
    bot_rocket = bot.Bot((100, 50, 155), 90, 200, 50, 150, 0, 0.08)
    # Бесконечный цикл программы
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_player.check_collision_with_mouse(pygame.mouse.get_pos()):
                    pygame.mouse.get_rel()
                    main_player.dragging = True
            if event.type == pygame.MOUSEBUTTONUP:
                main_player.dragging = False

        screen.fill((255, 255, 255))
        """Draw objects"""
        bot_rocket.draw(screen)
        main_player.draw(screen)
        gates1.draw(screen)
        gates2.draw(screen)
        middle.draw(screen)

        main_player.drag()
        game_ball.draw(screen)
        # Move objects
        game_ball.move()
        game_ball.change_direction_if_collision(main_player)
        game_ball.change_direction_if_collision(bot_rocket)
        bot_rocket.follow_ball(game_ball)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    print("Running")
    main()
