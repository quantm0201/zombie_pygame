import pygame, sys
from pygame.locals import *
import random

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 960
HEIGHT = 540

FPS = 60

# Zombie
Z_WIDTH = 200
Z_HEIGHT = 200
Z_TIME_APPEAR = 2
Z_TIME_DIE = 0.8
Z_MAX_NUMBER = 8

Z_NOT_SHOW_STATE = 0
Z_SHOW_STATE = 1
Z_DIE_STATE = 2

#Animation
Z_DIE_ANIM_FRAME = 8
EPS_ANIM_FRAME = 14

# Explosion

EPS_TIME_APPEAR = 0.5
SHOW_STATE = 0
NOT_SHOW_STATE = 1

# Attack
ATK_COOL_DOWN = 0.3
MAX_ANGLE = 20

#Game
DELTA_P_LOSE = 10

Z_DIE_ANIM = [[[], []], [[], []], [[], []]]

def loadDeadResource():
    for i in range(1, 4):
        for j in range(2):
            for k in range(1, Z_DIE_ANIM_FRAME + 1):
                image = pygame.image.load('res/Zombie/Zombie' + str(i) + '/animation/Dead' + str(k) + '.png')
                rect = image.get_rect()
                image = pygame.transform.scale(image, (rect.width // 3, rect.height // 3))
                if (j == 1):
                    image = pygame.transform.flip(image, True, False)
                Z_DIE_ANIM[i - 1][j].append(image)
NUM_BG = 4
NUM_DEAD_SOUND = 4
