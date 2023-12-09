import pygame
import math


class Inventory:
    def __init__(self):
        self.displaying = False
        self.size = 16
        self.items = []
        self.UIsize = pygame.Vector2(800, 600)
        self.backgroundColor = pygame.color.Color(156, 115, 26)

    def draw(self, screen: pygame.surface.Surface):
        if not self.displaying:
            return
        surf = pygame.surface.Surface(self.UIsize, pygame.SRCALPHA)

        pygame.draw.rect(surf, (0, 0, 0, 0),
                         pygame.rect.Rect(0, 0, self.UIsize.x, self.UIsize.y))  # draw transparent background
        pygame.draw.rect(surf, self.backgroundColor, pygame.rect.Rect(0, 0, self.UIsize.x, self.UIsize.y),
                         border_radius=30)

        tileSize = 64
        tileColor = pygame.color.Color(194, 158, 79)
        xOffset = math.floor((self.UIsize.x - (((math.floor(self.UIsize.x / (tileSize * 1.2))) * (tileSize * 1.2)) - (tileSize * 0.2))) /2) # do not fucking mess with this
        yOffset = math.floor((self.UIsize.y - (((math.floor(self.UIsize.y / (tileSize * 1.2))) * (tileSize * 1.2)) - (tileSize * 0.2))) /2)
        for x in range(math.floor(self.UIsize.x / (tileSize * 1.2))):
            for y in range(math.floor(self.UIsize.y / (tileSize * 1.2))):
                pygame.draw.rect(surf, tileColor,
                                 (xOffset + math.floor(x * tileSize * 1.2),yOffset + math.floor(y * tileSize * 1.2), tileSize, tileSize),
                                 border_radius=5)

        x, y = screen.get_rect().center
        pos = surf.get_rect(center=(x, y))
        screen.blit(surf, pos)


class Item:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.stackable = False
        self.amount = 1
        self.texture = pygame.image.load("sprites/empty.png")
