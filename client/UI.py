import pygame
from settingsManager import getSettings
import colors
getSettings()
pygame.font.init()
def render(screen:pygame.Surface,clock:pygame.time.Clock,player):
    settings = getSettings()
    font = pygame.font.Font(settings["FONT"],20)
    screen.blit(font.render(str(round(clock.get_fps(),1)),colors.BLACK,colors.TRANSPARENT),(10,10))
    screen.blit(font.render(str(player.rect.topleft), colors.BLACK, colors.TRANSPARENT), (10, 100))