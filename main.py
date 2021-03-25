import pygame, sys
from pygame.locals import *
import random
from Config import *
from Slot import *
from Point import *
from Mallet import *
from Explosion import *

def sortLayer(sprites):
    for zombie in sprites:
        posY = zombie.rect.top
        sprites.change_layer(zombie, posY)
    



pygame.init()

loadDeadResource()
pygame.mixer.music.load('res/sound/bgMusic.mp3')
pygame.mixer.music.play(-1)

hitSound = pygame.mixer.Sound('res/sound/hit1.wav')
deadSound = []
for x in range(4):
    ds = pygame.mixer.Sound('res/sound/dead' + str(x+1) + ".wav")
    deadSound.append(ds)
gOverSound = pygame.mixer.Sound('res/sound/gameOver.wav')
replaySound = pygame.mixer.Sound('res/sound/horrorLaugh.mp3')
replaySound.play()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

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

eps_group = pygame.sprite.LayeredUpdates()
eps = Explosion()
eps_group.add(eps)

point = Point()

loseNotice = pygame.font.SysFont('consolas', 30).render('Game Over!', True, WHITE)
loseNoticeRect = loseNotice.get_rect()
loseNoticeRect.center = (WIDTH//2, HEIGHT//2)
loseBackground = pygame.Surface((WIDTH, HEIGHT), SRCALPHA)
isEndGame = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            if isEndGame:
                loseBackground.fill((0, 0, 0, 0))
                isEndGame = False
                point.reset()
                replaySound.play()
                pygame.mixer.music.play(-1)
            else:
                pos = pygame.mouse.get_pos()
                mallet_group.sprites()[0].attack()
                hit = False
                for spr in zombie_group.sprites():
                    if spr.checkHit(pos):
                        print("hit")
                        hit = True
                        point.updatePoint(1)
                        eps_group.sprites()[0].show()
                        spr.die()
                        hitSound.play()
                        deadSound[random.randint(0, 3)].play()
                if hit == False:
                    point.updatePoint(0)
                if point.totalBeat - point.point >= DELTA_P_LOSE:
                    SCREEN.blit(backgroundMain, (0, 0))
                    point.draw(SCREEN)
                    loseBackground.fill((0, 0, 0, 50))
                    loseBackground.blit(loseNotice, loseNoticeRect)
                    SCREEN.blit(loseBackground, (0, 0))
                    isEndGame = True
                    gOverSound.play()
                    pygame.mixer.music.pause()
    
    if isEndGame == False:
    
        backgroundMain = pygame.transform.scale(background, (background.get_rect().width // 4, background.get_rect().height // 4))
        zombie_group.update()
        sortLayer(zombie_group)
            
        mallet_group.update()
        eps_group.update()
        zombie_group.draw(backgroundMain)
        eps_group.draw(backgroundMain)
        mallet_group.draw(backgroundMain)
        SCREEN.blit(backgroundMain, (0, 0))

        point.draw(SCREEN)
        
    pygame.display.update()
    clock.tick(FPS)