import pygame, sys
from pygame.locals import *
import random
from Config import *
from Slot import *
from Point import *
from Mallet import *

def sortLayer(sprites):
    for zombie in sprites:
        posY = zombie.rect.top
        sprites.change_layer(zombie, posY)
    



pygame.init()

SCREEN = pygame.display.set_mode((960, 540))

pygame.display.set_caption("BEAT THE ZOMBIE")

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


background = pygame.image.load("res/Object/background_1.png")

# mainGroup = pygame.sprite.Group()
# mainGroup.add(background)


# slot_group = pygame.sprite.LayeredUpdates()
zombie_group = pygame.sprite.LayeredUpdates()
for x in range(Z_MAX_NUMBER):
    # slot = Slot(x)
    # slot_group.add(slot)
    zombie = Zombie(x)
    zombie_group.add(zombie)

mallet_group = pygame.sprite.LayeredUpdates()
mallet = Mallet()
mallet_group.add(mallet)

point = Point()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            mallet_group.sprites()[0].attack()
            for spr in zombie_group.sprites():
                if spr.checkHit(pos):
                    print("hit")
                    point.updatePoint(1)
                    spr.die()
            
    
    backgroundMain = pygame.transform.scale(background, (background.get_rect().width // 4, background.get_rect().height // 4))
    zombie_group.update()
    sortLayer(zombie_group)

    mallet_group.update()
    zombie_group.draw(backgroundMain)
    mallet_group.draw(backgroundMain)
    SCREEN.blit(backgroundMain, (0, 0))
    
    point.draw(SCREEN)
    pygame.display.update()
        
    clock.tick(FPS)