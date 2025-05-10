import  pygame

pygame.init()


def ff():
    screen = pygame.display.set_mode((200, 200))
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render("Hello World!", True, (0, 0, 0))

    screen.fill((255, 255, 0))
    screen.blit(text_surface, (0, 100))

































