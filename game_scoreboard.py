import  pygame

pygame.init()

class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.bot_score = 0
        self.game_paused = False
        self.font = pygame.font.SysFont(None, 48)

    def game_pause(self):
        self.game_paused = True

    def update_player_score(self):
        self.game_pause()
        #TODO: Изменять счет игрока на 1

    def update_bot_score(self):
        self.game_pause()
        #TODO: Изменять счет бота на 1

    def draw_pause_screen(self, screen):
        #TODO: Создать окно паузы на котором будет текст со счетом и текст кто сейчас забил
        pass


# Не трогать
scoreboard = Scoreboard()

# Не трогать
def display_screen_overplay(screen, left_gate_scored = False, right_gate_scored = False):
    if left_gate_scored:
        scoreboard.update_player_score()
    elif right_gate_scored:
        scoreboard.update_bot_score()

    scoreboard.draw_pause_screen(screen)
    pygame.display.flip() # Update the screen

# Не нужна
def ff():
    screen = pygame.display.set_mode((200, 200))
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render("Hello World!", True, (0, 0, 0))

    screen.fill((255, 255, 0))
    screen.blit(text_surface, (0, 100))

































