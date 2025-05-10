import  pygame

pygame.init()

screen = pygame.display.set_mode((200,200))

while True:
        pygame.display.update()
        font = pygame.font.SysFont(None, 48)
        text_surface = font.render("Hello World!", True, (0, 0, 0))


        screen.fill((255, 255, 0))
        screen.blit(text_surface,(0,100))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()