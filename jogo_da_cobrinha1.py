#### 1 - Create empty window #####

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')


while True:
    for event in pygame.event.get():  # loop que controla eventos
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
