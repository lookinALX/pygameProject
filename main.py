import pygame
import shapes
import constants
import bot
import ball
import player
import gate
import game_scoreboard
pygame.init()


def main():
    # Ниже инициализация
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    gates1 = gate.Gate((100,50,155), 0,0 , 10,constants.SCREEN_HEIGHT )
    gates2 = gate.Gate((100,50,155), constants.SCREEN_WIDTH - 10,0 , 10,constants.SCREEN_HEIGHT )
    middle = shapes.Rectangle((0, 0, 255), 400, 0, 5, 600, 0, 0)
    game_ball = ball.Ball(color=(255, 0, 0), x=320, y=50, radius=20, speed_x=0.1 , speed_y=0.1)
    main_player = player.Player((255, 0, 255),700, 200, 50, 150, 0, 0)
    bot_rocket = bot.Bot((100, 50, 155), 50, 200, 50, 150, 0, 0.08)

    # шрифт
    #font = pygame.font.SysFont(None, 48)
    #text_surface = font.render("Hello World!", True, (0,0,0))
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_scoreboard.scoreboard.game_unpause()
                game_ball.x = constants.SCREEN_WIDTH // 2
                game_ball.y = constants.SCREEN_HEIGHT // 2
                game_ball.center = [game_ball.x , game_ball.y]

        screen.fill((255, 255, 255))
        """Draw objects"""

        #screen.blit(text_surface, (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2))

        bot_rocket.draw(screen)
        main_player.draw(screen)
        gates1.draw(screen)
        gates2.draw(screen)
        middle.draw(screen)

        main_player.drag()
        game_ball.draw(screen)

        if not game_scoreboard.scoreboard.game_paused:
            game_ball.move()
            game_ball.change_direction_if_collision(main_player)
            game_ball.change_direction_if_collision(bot_rocket)
            bot_rocket.follow_ball(game_ball)

            pygame.display.update()

            if gates1.score(game_ball):
                game_scoreboard.display_screen_overplay(screen, left_gate_scored = False, right_gate_scored = True)
                game_scoreboard.scoreboard.game_pause()
            if gates2.score(game_ball):
                game_scoreboard.display_screen_overplay(screen, left_gate_scored = True, right_gate_scored = False)
                game_scoreboard.scoreboard.game_pause()



if __name__ == "__main__":
    print("Running")
    main()
