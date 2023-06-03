import pygame
import city
class Gamestate:
    def __init__(self,grids,r,c):
        self.grids=grids
        self.r=r
        self.c=c
        self.state="start"
        self.player={"city":city.City(34,34,"images/cityplayer.png",100,self.grids)}
        self.debug = True
        self.set_water = True

    def update(self,screen,events):
        if self.state=="start":
            for i in range(40):
                for j in range(40):
                    if i < 30 or j < 30:
                        if self.debug == False:
                            self.grids[i][j].type = "hidden"
                        else:
                            pass
                    self.grids[i][j].draw(screen)
            self.player["city"].render(screen,self.grids)
        if self.set_water:
            self.set_grids_water(events)

    def set_grids_water(self,events):
        for i in range(40):
            for j in range(40):
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.grids[i][j].rect.collidepoint(event.pos):
                            with open("water.txt","w") as f:
                                f.write(str(i)+"," +str(j))

