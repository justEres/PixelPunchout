import pygame
import networking

class Player:
    def __init__(self, id):
        self.rect = pygame.rect.Rect(100, 100, 16, 16)
        self.lastRect = self.rect.copy()
        self.image = pygame.surface.Surface(self.rect.size)
        self.id = id
        self.scale = 5
        self.speed = 5

        self.loadImage()
        self.getRect()
        self.direction = pygame.Vector2(0,0)

    def update(self, server):
        newPosition = tuple(map(sum, zip(self.rect.topleft, self.direction * self.speed)))
        self.lastRect = self.rect.copy()
        self.rect.update(newPosition,self.rect.size)
        if not (self.rect == self.lastRect):
            args = (newPosition[0],newPosition[1])
            networking.packageSender("PLAYERPOS", args, server)



    def movement(self,event:pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.direction.y -= 1
            if event.key == pygame.K_s:
                self.direction.y += 1
            if event.key == pygame.K_a:
                self.direction.x -= 1
            if event.key == pygame.K_d:
                self.direction.x += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.direction.y += 1
            if event.key == pygame.K_s:
                self.direction.y -= 1
            if event.key == pygame.K_a:
                self.direction.x += 1
            if event.key == pygame.K_d:
                self.direction.x -= 1

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect.topleft)

    def getSourceImage(self):
        sourceImages = [
            "sprites/redPlayer.png",
            "sprites/bluePlayer.png",
            "sprites/greenPlayer.png"
        ]
        return sourceImages[self.id]

    def loadImage(self):
        self.image = pygame.image.load(self.getSourceImage())
        self.image = pygame.transform.scale(self.image,(self.scale * self.rect.size[0],self.scale * self.rect.size[1]))

    def getRect(self):
        self.rect = self.image.get_rect()
