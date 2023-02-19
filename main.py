import pygame as pg
import sys
from map import *


class Game:
    def __init__(self):
        pg.init()
        self.RES = width, height = 800 ,800
        self.screen = pg.display.set_mode(self.RES)
        self.newGame()
    
    def newGame(self):
        self.map = Map(self)

    def update(self):
        pg.display.flip()

    def draw(self):
        self.screen.fill('black')
        self.map.drawMap()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    def run(self):
        while True:
            self.checkEvents()
            self.draw()
            self.update()

if __name__ == '__main__':
    game = Game()
    game.run()