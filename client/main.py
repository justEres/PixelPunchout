import pygame
import settingsManager
import UI
import colors
def run():
    pygame.get_init()
    settings = settingsManager.getSettings()
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings['WINDOWWIDTH'],settings['WINDOWHEIGHT']))


    # GAMELOOP:
    while running:
        clock.tick(settings["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill(colors.WHITE)
        UI.render(screen,clock)
        pygame.display.flip() #update screen

if __name__ == "__main__":
    run()