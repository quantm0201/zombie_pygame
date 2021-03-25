import pygame, sys
from pygame.locals import *
from Config import *

class Point():
    def __init__(self):
        self.point = 0
        self.totalBeat = 0

    def updatePoint(self, point):
        self.totalBeat += 1
        self.point += point

    def reset(self):
        self.totalBeat = 0
        self.point = 0

    def draw(self, surface):
        font = pygame.font.SysFont('consolas', 30)
        self.surface = font.render('Point: ' + str(self.point) + '/' + str(self.totalBeat), True, WHITE)
        self.rect = self.surface.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT//6)
        surface.blit(self.surface, self.rect)