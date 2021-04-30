import pygame


class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.filePaths = [f"./assets/girlWalk{counter}.png" for counter in range(4)]
        self.moving = False
        self.movingTo = (None, None)



    def draw(self, screen):
        player = pygame.image.load(self.filePaths[0]).convert_alpha()
        # player = pygame.transform.scale(player, (90, 120))
        screen.blit(player, [self.x, self.y])


    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10


    def moveTo(self, mousePos):
        self.movingTo = mousePos
        self.moving = True



    def update(self):
        if (self.moving):
            if (self.movingTo[0] < self.x):
                self.x -= 2
            if (self.movingTo[0] > self.x):
                self.x += 2
            if (self.movingTo[1] < self.y):
                self.y -= 2
            if (self.movingTo[1] > self.y):
                self.y += 2