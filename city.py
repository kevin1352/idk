import pygame
class City:
    def __init__(self,r,c,image,health,grids):
        self.r=r
        self.c=c
        self.image=pygame.image.load(image)
        self.health=health
        for i in range(4):
            for j in range(4):
                grids[self.r+i][self.c+j].type = "city"
    def render(self,screen,grids):
        pos=[grids[self.r][self.c].x,grids[self.r][self.c].y]
        screen.blit(self.image,pos)