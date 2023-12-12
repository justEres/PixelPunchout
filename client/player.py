import pygame
import networking
import controller

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
        if not self.direction == pygame.Vector2(0,0):
            direction = self.direction.normalize()
        else:
            direction = pygame.Vector2(0,0)

        newPosition = tuple(map(sum, zip(self.rect.topleft, direction * self.speed)))

        self.lastRect = self.rect.copy()

        self.rect.update(newPosition,self.rect.size)
        if not (self.rect == self.lastRect):
            args = (newPosition[0],newPosition[1])
            if server == "offline":
                return
            networking.packageSender(self.id ,"PLAYERPOS", args, server)


    def setPos(self,pos: pygame.Vector2):
        self.rect.update(pos, self.rect.size)

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
        if controller.jcount > 0:
            direction = controller.getVec(event)
            direction += self.nearly00(direction)
            self.direction = direction.normalize()


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

    def nearly00(self, vec:pygame.Vector2):
        if -0.3 <= vec.x <= 0.3:
            x = 0
        else:
            x = vec.x
        if -0.3 <= vec.y <= 0.3:
            y = 0
        else:
            y = vec.y
        return pygame.Vector2(x,y)