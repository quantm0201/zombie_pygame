import pygame, sys
from pygame.locals import *
import random
from Config import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self, id):
        pygame.sprite.Sprite.__init__(self)

        self.id = id
        self.deadSprites = []
        for i in range(1, Z_DIE_ANIM_FRAME + 1):
            image = pygame.image.load('res/Zombie/Zombie1/animation/Dead' + str(i) + '.png')
            rect = image.get_rect()
            self.deadSprites.append(pygame.transform.scale(image, (rect.width // 3, rect.height // 3)))  

        self.spr1 = pygame.image.load('res/Zombie/Zombie1/animation/Walk1.png').convert()
        self.spr1.set_colorkey(BLACK)
        self.image = self.spr1
        self.rec1 = self.spr1.get_rect()
        self.rect = Rect(self.getRandomPos(), (self.rec1.width // 3, self.rec1.height // 3))
        self.bottomPoint = self.rect.bottom

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
        posY = self.bottomPoint - rectImage.height
        self.rect = Rect(self.rect.left, posY, rectImage.width, rectImage.height)



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



