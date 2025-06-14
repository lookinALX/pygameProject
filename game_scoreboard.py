import  pygame

import constants

pygame.init()

class Scoreboard:
    def __init__(self):
        self.player_score = 0
        self.bot_score = 0
        self.game_paused = False
        self.game_score = True
        self.font = pygame.font.SysFont(None, 48)
        self.sco = False
        self.sc = False
    def game_pause(self):
        self.game_paused = True

    def game_unpause(self):
        self.game_paused = False

    def update_player_score(self):
        self.game_pause()
        self.player_score += 1

    def update_bot_score(self):
        self.game_pause()
        self.bot_score += 1

    def draw_pause_screen(self, screen ):

        overlay = pygame.Surface((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0,0,0, 150))
        screen.blit(overlay,(0,0))
        tex = (f" БОТ {self.bot_score}: {self.player_score} ИГРОК")


        font = pygame.font.SysFont(None, 48)
        text_surface = font.render(tex,True, (111, 0, 0))
        screen.blit(text_surface, (200, 350))










        # TODO: ВЫВЕСТИ ТЕКСТ ГОЛ И СЧЕТ!




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

































