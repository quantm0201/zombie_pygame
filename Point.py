import pygame, sys
from pygame.locals import *
from Config import *

class Point():
    def __init__(self):
        self.point = 0
        self.x = 3*Z_WIDTH
        self.y = Z_HEIGHT/2
        font = pygame.font.SysFont('consolas', 30)
        self.surface = font.render('Point: ' + str(self.point), True, BLACK)

    def updatePoint(self, point):
        self.point += point

    def draw(self, surface):
        font = pygame.font.SysFont('consolas', 30)
        self.surface = font.render('Point: ' + str(self.point), True, BLACK)
        surface.blit(self.surface, (self.x, self.y))