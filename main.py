import pygame
from pygame.locals import *
from random import randint

import gamelib
from element import Player, Bomb, Wall

class MainGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    bomb_number = 3
    blast_color_check = 0
    def __init__(self):
        color_random = randint(0,1)
        if(color_random is 0):
            MainGame.blast_color_check = 0
            super(MainGame, self).__init__('MainGame', MainGame.WHITE)
        elif(color_random is 1):
            MainGame.blast_color_check = 1
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
                color_random = randint(0,1)
                if(color_random is 0):
                    color = 0
                elif(color_random is 1):
                    color = 1
                self.world_map[i][j] = Wall((wall_x,wall_y),color)
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

        self.player.check_offscreen()
        self.player.player_move_delay()

        if self.player.delay <= 0:
            if self.is_key_pressed(K_UP):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player.x,self.player.y,0,-75) ):
                            collide = True
                if not collide:
                    self.player.move_up()

            elif self.is_key_pressed(K_DOWN):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player.x,self.player.y,0,+75) ):
                            collide = True
                if not collide:
                    self.player.move_down()

            elif self.is_key_pressed(K_LEFT):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player.x,self.player.y,-75,0) ):
                            collide = True
                if not collide:
                    self.player.move_left()
            elif self.is_key_pressed(K_RIGHT):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player.x,self.player.y,+75,0) ):
                            collide = True
                if not collide:
                    self.player.move_right() #movement



        for k in range(0,self.bomb_number,1):

            self.bomb[k].check_blast_color(MainGame.blast_color_check)

            if (self.is_key_pressed(K_SPACE) and (self.bomb[k].isbomb is True)):
                self.bomb[k].plant_bomb(self.player.get_x(), self.player.get_y())
            check = 0
            for i in range(0,20,2):
                for j in range(0,14,2):
                    if ( self.world_map[i][j].collision(self.bomb[k].x,self.bomb[k].y,+75,0) ):
                        check = 1
                        self.bomb[k].check_blast_x_collide = True
                    if check is 0:
                        self.bomb[k].check_blast_x_collide = False
                    if ( self.world_map[i][j].collision(self.bomb[k].x,self.bomb[k].y,0,-75) ):
                        check = 1
                        self.bomb[k].check_blast_y_collide = True
                    if check is 0:
                        self.bomb[k].check_blast_y_collide = False
            self.bomb[k].bomb_decay()
            self.bomb[k].bomb_blast()

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