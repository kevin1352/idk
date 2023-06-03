import pygame
class Grid:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.type=None
        self.rect=pygame.Rect([self.x,self.y],[self.w,self.h])
        self.image = pygame.image.load("images/fog.png")

    def draw(self,screen):
        if self.type==None:
            pygame.draw.rect(screen,(0,0,0),self.rect,width=1)
        elif self.type == "city":
            pygame.draw.rect(screen,(255,255,255),self.rect)
        elif self.type == "hidden":
            screen.blit(self.image,[self.x,self.y])


def createGrids(startx,starty,w,h,endx,endy):
    grids=[]
    x = startx
    y = starty
    i = 0
    j = 0
    while y < endy:
        grids.append([])
        while x < endx:
            grids[i].append(Grid(x,y,w,h))
            x += w
        x = startx
        i += 1
        y += h
    return grids
