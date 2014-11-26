import pygame
from pygame.locals import *

import gamelib
from element import Player, Bomb, Wall

class MainGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    bomb_number = 3
    def __init__(self):
        super(MainGame, self).__init__('MainGame', MainGame.BLACK)
        self.player= Player(radius=30,
                         color=MainGame.WHITE,
                         pos=(532,
                              382))
        self.bomb = []
        for i in range(0,self.bomb_number,1):
            self.bomb.append(i)
            self.bomb[i] = Bomb()

        self.world_map = []
        for i in range(0,20,1):
            self.world_map.append(i)
            self.world_map[i] = []
            for j in range(0,14,1):
                self.world_map[i].append(j)
        wall_x = 0
        wall_y = 0
        for i in range(0,20,2):
            for j in range(0,14,2):
                self.world_map[i][j] = Wall((wall_x,wall_y), MainGame.WHITE)
                wall_x += 152
                if(wall_x > 1280):
                    wall_x = 0
                    wall_y += 152





    def init(self):
        super(MainGame, self).init()

    def update(self):
        if self.is_key_pressed(K_ESCAPE):
            print "terminate by user...."
            self.terminate()

        self.player.check_move()
        self.player.player_delay()
        if self.player.delay <= 0:
            if self.is_key_pressed(K_UP):
                self.player.move_up()
            elif self.is_key_pressed(K_DOWN):
                self.player.move_down()
            elif self.is_key_pressed(K_LEFT):
                self.player.move_left()
            elif self.is_key_pressed(K_RIGHT):
                self.player.move_right()


            for i in range(0,20,2):
                for j in range(0,14,2):
                    self.world_map[i][j].collision(self.player)

        if (self.is_key_pressed(K_SPACE) and (self.bomb[0].isbomb is True)):
            self.bomb[0].plant_bomb(self.player.get_x(), self.player.get_y())
        elif (self.is_key_pressed(K_SPACE) and (self.bomb[1].isbomb is True)):
            self.bomb[1].plant_bomb(self.player.get_x(), self.player.get_y())
        elif (self.is_key_pressed(K_SPACE) and (self.bomb[2].isbomb is True)):
            self.bomb[2].plant_bomb(self.player.get_x(), self.player.get_y())

        for x in range(0,self.bomb_number,1):
            self.bomb[x].bomb_decay()
            self.bomb[x].bomb_blast()

    def render(self, surface):
        self.player.render(surface)
        for x in range(0,self.bomb_number,1):
            self.bomb[x].render(surface)
        for i in range(0,20,2):
            for j in range(0,14,2):
                self.world_map[i][j].render(surface)

def main():
    game = MainGame()
    game.run()

if __name__ == '__main__':
    main()