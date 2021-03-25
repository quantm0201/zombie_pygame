import pygame, sys
from pygame.locals import *
import random
from Config import *

class Mallet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.originImage = pygame.image.load("res/Object/mallet.png")
        self.image = pygame.image.load("res/Object/mallet.png")
        self.size = self.image.get_size()
        pos = pygame.mouse.get_pos()
        self.rect = Rect(pos, self.size) 
        self.rect.center = (pos[0] + self.rect.width, pos[1] + self.rect.height / 2)
        self.isRunning = False
        self.coolDown = 0

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect = Rect(pos, self.size) 
        self.rect.center = (pos[0] + self.rect.width / 4, pos[1] + self.rect.height / 4)

        if (self.coolDown > 0):
            self.coolDown -= 1

        if (self.coolDown == 0):
            self.isRunning = False

        if (self.coolDown < ATK_COOL_DOWN * FPS / 2):
            angle = MAX_ANGLE * (self.coolDown / (ATK_COOL_DOWN * FPS/ 2))
            self.image = pygame.transform.rotate(self.originImage, angle)
        else:
            angle = (ATK_COOL_DOWN * FPS - self.coolDown) / (ATK_COOL_DOWN  * FPS / 2) * MAX_ANGLE
            self.image = pygame.transform.rotate(self.originImage, angle)
    

    def attack(self):
        if (self.isRunning):
            return
        
        self.isRunning = True
        self.coolDown = ATK_COOL_DOWN * FPS