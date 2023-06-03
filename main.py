import pygame
from grid import *
import gamestate

pygame.init()
screen=pygame.display.set_mode([800,800])
clock=pygame.time.Clock()
backround=pygame.image.load("images/backround.png")

grids = createGrids(0,0,20,20,800,800)
print(len(grids))
gamestate1=gamestate.Gamestate(grids,40,40)


fps = 60
isRunning=True
while isRunning:
    events=pygame.event.get()
    for event in  events:
        if event.type==pygame.QUIT:
            isRunning=False
    screen.fill((255,255,255))
    screen.blit(backround,[0,0])
    gamestate1.update(screen,events)



    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
