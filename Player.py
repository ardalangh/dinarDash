import pygame


class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.moving = False
        self.movingTo = (None, None)
        self.dir = "RIGHT"
        self.img_counter = 0




    def get_file_path(self):
        return f"./assets/girlWalk{self.dir}{self.img_counter}.png"

    def draw(self, screen):
        print(self.get_file_path())
        player = pygame.image.load(self.get_file_path()).convert_alpha()
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
                self.dir = "LEFT"
                self.x -= 5
            if (self.movingTo[0] > self.x):
                self.dir = "RIGHT"
                self.x += 5
            if (self.movingTo[1] < self.y):
                self.y -= 5
            if (self.movingTo[1] > self.y):
                self.y += 5
            self.img_counter = (self.img_counter + 1) % 4

            if (abs(self.movingTo[1] - self.y) <5 and abs(self.movingTo[0] - self.x) < 5):
                self.moving = False;
