import pygame as pg
import sys
from settings import *
from mapGame import *

class Game:
    def __init__(self):
       #Criar a tela para renderizar a resolução do jogo 
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)

    #Atualização da tela para mostrar os FPS
    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')
    
    #A cada interação pintar a tela de preto
    def draw(self):
        self.screen.fill('black')
        self.map.draw()
    
    #Checar eventos por ex se apertamos a tecla ESC para sair do game
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
 