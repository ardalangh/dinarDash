import pygame


class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.filePaths = [f"./assets/girlWalk{counter}.png" for counter in range(4)]



    def draw(self, screen):
        player = pygame.image.load(self.filePaths[0]).convert_alpha()
        # player = pygame.transform.scale(player, (90, 120))
        screen.blit(player, [self.x, self.y])


    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10