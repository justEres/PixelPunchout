import pygame
import settingsManager
import UI
import colors
import player
import networking
import inventory

def run():
    pygame.get_init()
    settings = settingsManager.getSettings()
    server = networking.init(newPlayerFunc, setPlayerPosFunc)
    running = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((settings['WINDOWWIDTH'], settings['WINDOWHEIGHT']))

    global players
    players = [player.Player(0)]
    inv = inventory.Inventory()

    # GAMELOOP:
    while running:
        clock.tick(settings["FPS"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    inv.displaying = not inv.displaying
                    print(inv.displaying)

            players[0].movement(event)
        players[0].update(server)

        screen.fill(colors.WHITE)


        inv.draw(screen)

        for p in players:
            p.render(screen)

        UI.render(screen, clock, players[0])
        pygame.display.flip()  # update screen


def newPlayerFunc(id):
    players.append(player.Player(id))


def setPlayerPosFunc(id, args):
    players[id].setPos(pygame.Vector2(args))


if __name__ == "__main__":
    run()
