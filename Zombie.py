import pygame, sys
from pygame.locals import *
import random
from Config import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        self.id = id
        
        typeZombie = random.randint(1, 3)
        self.flip = random.randint(0, 1)
        self.deadSprites = Z_DIE_ANIM[typeZombie - 1][self.flip]

        typePosture = random.randint(1, 4)
        self.spr1 = pygame.image.load('res/Zombie/Zombie' + str(typeZombie) + '/animation/Stand' + str(typePosture) + '.png').convert()
        if (self.flip == 1):
            self.spr1 = pygame.transform.flip(self.spr1, True, False)

        self.spr1.set_colorkey(BLACK)
        self.image = self.spr1
        self.rec1 = self.spr1.get_rect()
        self.rect = Rect(self.getRandomPos(), (self.rec1.width // 3, self.rec1.height // 3))
        self.bottomPoint = self.rect.bottom
        self.rightPoint = self.rect.right

        self.state = Z_NOT_SHOW_STATE
        self.timeRemain = 0

    def die(self):
        self.state = Z_DIE_STATE
        self.timeRemain = Z_TIME_DIE * FPS
        # self.image = pygame.transform.scale(self.spr2, (self.rec2.width//3, self.rec2.height//3))
        # self.rect = self.image.get_rect()
        # self.rect.center = (Z_WIDTH//2, Z_HEIGHT*3/4)

    def respawn(self):
        self.state = Z_SHOW_STATE
        self.timeRemain = Z_TIME_APPEAR * FPS
        self.image = pygame.transform.scale(self.spr1, (self.rec1.width//3, self.rec1.height//3))
        self.image.set_alpha(255)
        # self.rect = self.image.get_rect()
        self.rect = Rect(self.getRandomPos(), (self.rec1.width // 3, self.rec1.height // 3))
        self.bottomPoint = self.rect.bottom
        self.rightPoint = self.rect.right

        # self.rect.center = (Z_WIDTH//2, Z_HEIGHT//2)

    def checkHit(self, pos):
        if (self.timeRemain > 0 and self.state == Z_SHOW_STATE):
            headRect = Rect(self.rect.left, self.rect.top, self.rect.width, self.rect.height / 3)
            return headRect.collidepoint(pos)

    def getRandomPos(self):
        ranX = random.randint(0, 900)
        ranY = random.randint(150, 330)
        return (ranX, ranY)

    def runDeadAnimation(self):
        timePerFrame = Z_TIME_DIE * FPS / Z_DIE_ANIM_FRAME
        animState = Z_DIE_ANIM_FRAME - self.timeRemain // timePerFrame
        self.image = self.deadSprites[int(animState - 1)]

        rectImage = self.image.get_rect()
        posX = self.rect.left
        if (self.flip):
            posX = self.rightPoint - rectImage.width
        posY = self.bottomPoint - rectImage.height
        self.rect = Rect(posX, posY, rectImage.width, rectImage.height)



    def update(self):
        if (self.state == Z_NOT_SHOW_STATE):
            self.image.set_alpha(0)
            if (random.randint(0, 2 * FPS) == FPS):
                self.respawn()

        if (self.timeRemain > 0):
            self.timeRemain -= 1

        if (self.timeRemain == 0):
            self.state = Z_NOT_SHOW_STATE

        if (self.state == Z_SHOW_STATE):
            return
        elif (self.state == Z_DIE_STATE):
            self.runDeadAnimation()
        else:       # Z_NOT_SHOW_STATE
            return



