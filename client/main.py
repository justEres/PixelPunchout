import pygame
import settingsManager
import UI
import colors
import player


def run():
    pygame.get_init()
    settings = settingsManager.getSettings()
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings['WINDOWWIDTH'], settings['WINDOWHEIGHT']))
    player0 = player.Player(0)


    # GAMELOOP:
    while running:
        clock.tick(settings["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            player0.movement(event)
        player0.update()

        screen.fill(colors.WHITE)


        player0.render(screen)
        UI.render(screen, clock,player0)
        pygame.display.flip()  # update screen


if __name__ == "__main__":
    run()
