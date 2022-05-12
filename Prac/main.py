import pygame as pg
import sys
from map import *
from level import Level

class Main:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Demo")
        self.clock = pg.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            
            self.screen.fill('sky blue')
            self.level.run()
            self.clock.tick(FPS)
            pg.display.update()

if __name__ == '__main__':
    Main().run()
