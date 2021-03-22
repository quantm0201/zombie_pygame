import pygame, sys
from pygame.locals import *
import random
from Config import *
from Slot import *
from Point import *

pygame.init()

SCREEN = pygame.display.set_mode((800, 600))

pygame.display.set_caption("BEAT THE ZOMBIE")

clock = pygame.time.Clock()





slot_group = pygame.sprite.Group()
zombie_group = pygame.sprite.Group()
for x in range(9):
    slot = Slot(x)
    slot_group.add(slot)
    zombie_group.add(slot.zombie)

point = Point()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for spr in slot_group.sprites():
                if spr.checkHit(pos):
                    point.updatePoint(1)
                    spr.killZombie()
            

    slot_group.update()
    zombie_group.update()

    SCREEN.fill(WHITE)
    slot_group.draw(SCREEN)
    
    point.draw(SCREEN)
    pygame.display.update()
        
    clock.tick(FPS)