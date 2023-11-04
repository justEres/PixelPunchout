import pygame
import settingsManager


def run():
    pygame.get_init()
    settings = settingsManager.getSettings()
    running = True
    print(settings)
    screen = pygame.display.set_mode((settings['WINDOWWIDTH'],settings['WINDOWHEIGHT']))


    # GAMELOOP:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.flip() #update screen

if __name__ == "__main__":
    run()