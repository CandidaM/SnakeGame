#### 3 -   Add clock #####

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

snake = [(200, 200), (210, 200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))




clock = pygame.time.Clock()

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        
    for pos in snake:
        screen.blit(snake_skin,pos)




    pygame.display.update()