import pygame as pg

_ = False
minimap = [[1,1,1,1,1,1,1,1,1,1],
           [1,_,_,1,1,_,_,_,_,1],
           [1,_,_,1,1,_,1,1,_,1],
           [1,_,_,_,_,_,1,1,_,1],
           [1,_,1,1,1,_,_,_,_,1],
           [1,_,1,1,1,1,_,1,1,1],
           [1,_,1,1,1,1,_,1,1,1],
           [1,_,_,_,_,_,_,1,1,1],
           [1,_,_,_,_,_,_,1,1,1],
           [1,1,1,1,1,1,1,1,1,1]]

class Map:
    def __init__(self, game):
        self.minimap = minimap
        self.game = game

    def drawMap(self):
        for i in range(len(self.minimap)):
            for j in range(len(self.minimap[i])):
                if self.minimap[i][j] == 1:
                    pg.draw.rect(self.game.screen, 'darkgray', (i*80, j*80, 80,80),2)