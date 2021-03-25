import pygame, sys
from pygame.locals import *
import random
from Config import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.epsSprite = []
        for i in range(1, EPS_ANIM_FRAME + 1):
            image = pygame.image.load('res/Explosion/ex' + str(i) + '.png')
            rect = image.get_rect()
            image = pygame.transform.scale(image, (rect.width // 3, rect.height // 3))
            self.epsSprite.append(image)
        
        self.state = NOT_SHOW_STATE
        self.image = self.epsSprite[0]
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.timeRemain = 0

    def hide(self):
        self.state = NOT_SHOW_STATE
        self.image.set_alpha(0)

    def show(self):
        self.state = SHOW_STATE
        self.image.set_alpha(255)
        self.timeRemain = EPS_TIME_APPEAR * FPS
        self.appearPosition = pygame.mouse.get_pos()

    def runEPSAnimation(self):
        timePerFrame = EPS_TIME_APPEAR * FPS / EPS_ANIM_FRAME
        animState = EPS_ANIM_FRAME - self.timeRemain // timePerFrame
        self.image = self.epsSprite[int(animState - 1)]

        rectImage = self.image.get_rect()
        pos = (self.appearPosition[0] - rectImage.width / 2
        , self.appearPosition[1] - rectImage.height / 2)
        self.rect = Rect(pos, (rectImage.width, rectImage.height))

    def update(self):
        if (self.timeRemain > 0):
            self.timeRemain -= 1

        if (self.timeRemain == 0):
            self.hide()

        if (self.state == SHOW_STATE):
            self.runEPSAnimation()