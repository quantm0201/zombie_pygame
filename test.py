import pygame
pygame.init()
screen = pygame.display.set_mode((800 , 600))


class Actor(pygame.sprite.Sprite):
    def __init__(self, group, color, layer, pos, width, height, add):
        # self.image = pygame.Surface((width, height))
        self.image = pygame.image.load(add)
        self.rect = pos
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, group)

class Actor2(pygame.sprite.Sprite):
    def __init__(self, color, layer):
        # self.image = pygame.Surface((width, height))
        self.image = pygame.Surface((400, 400))
        self.image.fill(color)
        self.rect = (200, 200)
        self._layer = layer

        self.group = pygame.sprite.LayeredUpdates()
        Actor(self.group, (255, 255, 255), 0, (0, 0), 200, 200, "res/Zombie/Zombie1/animation/Dead1.png")
        Actor(self.group, (255, 0, 255),   1, (0, 0), 30, 30, "res/Zombie/Zombie1/animation/Dead2.png")
        self.group.draw(self.image)

        pygame.sprite.Sprite.__init__(self)

image = Actor2((0, 255, 0), -1)
image2 = Actor2((255, 0, 0), 1)
image2.rect = (0, 0)
image_gr = pygame.sprite.LayeredUpdates()
image_gr.add(image)
image_gr.add(image2)
# Actor(group, (0, 255, 255),   0, (120, 120))
# Actor(group, (255, 255, 0),   3, (130, 130))
# Actor(group, (0, 0, 255),     2, (140, 140))

run = True
while run:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            run = False
    screen.fill((255,0,0))
    image_gr.draw(screen)
    pygame.display.flip()