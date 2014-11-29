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
    player_number = 2
    blast_color_check = 0
    player_default_pos = (532,382)
    def __init__(self):
        color_random = randint(0,1)
        if(color_random is 0):
            MainGame.blast_color_check = 0
            super(MainGame, self).__init__('MainGame', MainGame.WHITE)
        elif(color_random is 1):
            MainGame.blast_color_check = 1
            super(MainGame, self).__init__('MainGame', MainGame.BLACK)

        self.player = []
        for i in range(0,self.player_number,1):
            self.player.append(Player(radius=30,
                         color=MainGame.WHITE,
                         pos=self.player_default_pos))
            self.player_default_pos = (532+152,382+152)

        self.bomb = []
        for i in range(0,self.bomb_number,1):
            self.bomb.append(i)
            self.bomb[i] = Bomb()


        self.bomb2 = []
        for i in range(0,self.bomb_number,1):
            self.bomb2.append(i)
            self.bomb2[i] = Bomb()


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

    def pbomb(self):
        print self.bomb[0].send_blast_status()
        print self.bomb[1].send_blast_status()
        print self.bomb[2].send_blast_status()





    def init(self):
        super(MainGame, self).init()

    def update(self):
        if self.is_key_pressed(K_ESCAPE):
            print "terminate by user...."
            self.terminate()

        self.player[0].check_offscreen()
        self.player[0].player_move_delay()

        if self.player[0].delay <= 0:
            if self.is_key_pressed(K_w):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,0,-75) ):
                            collide = True
                if not collide:
                    self.player[0].move_up()

            elif self.is_key_pressed(K_s):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,0,+75) ):
                            collide = True
                if not collide:
                    self.player[0].move_down()

            elif self.is_key_pressed(K_a):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,-75,0) ):
                            collide = True
                if not collide:
                    self.player[0].move_left()
            elif self.is_key_pressed(K_d):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,+75,0) ):
                            collide = True
                if not collide:
                    self.player[0].move_right() #movement

                self.player[0].check_offscreen()

        self.player[1].check_offscreen()
        self.player[1].player_move_delay()

        if self.player[1].delay <= 0:
            if self.is_key_pressed(K_UP):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,0,-75) ):
                            collide = True
                if not collide:
                    self.player[1].move_up()

            elif self.is_key_pressed(K_DOWN):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,0,+75) ):
                            collide = True
                if not collide:
                    self.player[1].move_down()

            elif self.is_key_pressed(K_LEFT):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,-75,0) ):
                            collide = True
                if not collide:
                    self.player[1].move_left()
            elif self.is_key_pressed(K_RIGHT):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,+75,0) ):
                            collide = True
                if not collide:
                    self.player[1].move_right() #movement

        for k in range(0,self.bomb_number,1): #bombloop

            self.bomb[k].check_blast_color(MainGame.blast_color_check)

            if (self.is_key_pressed(K_SPACE) and not self.bomb[k].isPlant ) :
                self.bomb[k].plant_bomb(self.player[0].get_x(), self.player[0].get_y())

            self.bomb[k].bomb_decay()
            self.bomb[k].bomb_blast()
            for i in range(0,self.player_number,1):
                self.bomb[k].check_player(self.player[i])

        for k in range(0,self.bomb_number,1): #bombloop

            self.bomb[k].check_blast_color(MainGame.blast_color_check)

            if (self.is_key_pressed(K_RCTRL) and not self.bomb[k].isPlant ) :
                self.bomb[k].plant_bomb(self.player[1].get_x(), self.player[1].get_y())

            self.bomb[k].bomb_decay()
            self.bomb[k].bomb_blast()
            for i in range(0,self.player_number,1):
                self.bomb[k].check_player(self.player[i])


    def render(self, surface):
        for i in range(0,self.player_number,1):
            self.player[i].render(surface)
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