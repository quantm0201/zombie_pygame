import pygame, sys
from pygame.locals import *
import random
from Config import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.spr1 = pygame.image.load('res/Zombie/Zombie1/animation/Walk1.png').convert()
        self.spr1.set_colorkey(WHITE)
        self.rec1 = self.spr1.get_rect()
        self.spr2 = pygame.image.load('res/Zombie/Zombie1/animation/Dead7.png').convert()
        self.spr2.set_colorkey(WHITE)
        self.rec2 = self.spr2.get_rect()
        self.image = pygame.transform.scale(self.spr1, (self.rec1.width//3, self.rec1.height//3))
        self.rect = self.image.get_rect()
        self.rect.center = (Z_WIDTH//2, Z_HEIGHT//2)

    def die(self):
        self.image = pygame.transform.scale(self.spr2, (self.rec2.width//3, self.rec2.height//3))
        self.rect = self.image.get_rect()
        self.rect.center = (Z_WIDTH//2, Z_HEIGHT*3/4)

    def respawn(self):
        self.image = pygame.transform.scale(self.spr1, (self.rec1.width//3, self.rec1.height//3))
        self.rect = self.image.get_rect()
        self.rect.center = (Z_WIDTH//2, Z_HEIGHT//2)

    def update(self):
        self.rect.y -= 0