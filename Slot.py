import pygame, sys
from pygame.locals import *
import random
from Config import *
from Zombie import *

class Slot(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        self.id = id
        
        self.image = pygame.Surface((Z_WIDTH, Z_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        x = self.getPos()[0]
        y = self.getPos()[1]
        self.rect.center = (x + self.rect.width/2, y + self.rect.height/2)

        self.zombie = Zombie()

        self.timeRemain = 0

    def getPos(self):
        switcher = {
            0: (0, 0),
            1: (Z_WIDTH, 0),
            2: (2*Z_WIDTH, 0),
            3: (0, Z_HEIGHT),
            4: (Z_WIDTH, Z_HEIGHT),
            5: (2*Z_WIDTH, Z_HEIGHT),
            6: (0, 2*Z_HEIGHT),
            7: (Z_WIDTH, 2*Z_HEIGHT),
            8: (2*Z_WIDTH, 2*Z_HEIGHT)
        }
        return switcher.get(self.id, (0, 0))

    def checkHit(self, pos):
        if self.timeRemain > 0:
            return self.rect.collidepoint(pos)
        return False

    def killZombie(self):
        self.zombie.die()
        self.image.fill(GREEN)
        self.image.blit(self.zombie.image, self.zombie.rect)

    def update(self):
        if (self.timeRemain > 0):
            self.timeRemain -= 1
            return
        if random.randint(0, 6*FPS) == FPS:
            self.zombie.respawn()
            self.image.blit(self.zombie.image, self.zombie.rect)
            self.timeRemain = Z_TIME_APPEAR*FPS
        else:
            self.image.fill(GREEN)
            self.isShow = False