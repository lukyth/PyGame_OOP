import pygame
from pygame.locals import *
from random import randint
from board.practicum import findDevices
from board.peri import PeriBoard

import gamelib
from element import Player, Bomb, Wall

class MainGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    BG = pygame.Color('black')
    BG_for_player = 1
    bomb_number = 3
    player_number = 2
    blast_color_check = 0
    player_default_pos = (532,382)
    def __init__(self):

        super(MainGame, self).__init__('MainGame', MainGame.BLACK)


        self.player = []
        for i in range(0,self.player_number,1):
            board = None
            if i < len(findDevices()):
                board = PeriBoard(findDevices()[i])
            self.player.append(Player(board,radius=30,color=MainGame.WHITE,pos=self.player_default_pos))
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

        print "Who died more than 5 times LOSE!!"

    def pbomb(self):
        print self.bomb[0].send_blast_status()
        print self.bomb[1].send_blast_status()
        print self.bomb[2].send_blast_status()


    def get_switch(self, switch, player):
        board = self.player[player].board
        if board is not None:
            if switch is 'up':
                return board.getSwitchUp()
            elif switch is 'down':
                return board.getSwitchDown()
            elif switch is 'left':
                return board.getSwitchLeft()
            elif switch is 'right':
                return board.getSwitchRight()
            elif switch is 'bomb':
                return board.getSwitchBomb()
        return False

    def get_light(self, player):
        board = self.player[player].board
        if board is not None:
            return board.getLight()
        return 500

    def init(self):
        super(MainGame, self).init()

    def update(self):
        self.get_BG_color(self.BG)
        if self.is_key_pressed(K_ESCAPE) or self.player[0].game_end is 1 or self.player[1].game_end is 1:
            print "terminate by user...."
            self.terminate()

        if(self.player[0].BG_delay < 0):#BG_CHANGE_FOR_OOP P1
            if self.is_key_pressed(K_q) or self.get_light(0) < 150:
                if(MainGame.BG_for_player is 0):
                    MainGame.BG = MainGame.BLACK
                    MainGame.BG_for_player = 1
                    self.player[0].BG_delay = self.player[0].init_BG_delay
                elif(MainGame.BG_for_player is 1):
                    MainGame.BG =  MainGame.WHITE
                    MainGame.BG_for_player = 0
                    self.player[0].BG_delay = self.player[0].init_BG_delay

        if(self.player[1].BG_delay < 0):#BG_CHANGE_FOR_OOP P2
            if self.is_key_pressed(K_RSHIFT)  or self.get_light(1) < 150:
                if(MainGame.BG_for_player is 0):
                    MainGame.BG = MainGame.BLACK
                    MainGame.BG_for_player = 1
                    self.player[1].BG_delay = self.player[0].init_BG_delay
                elif(MainGame.BG_for_player is 1):
                    MainGame.BG =  MainGame.WHITE
                    MainGame.BG_for_player = 0
                    self.player[1].BG_delay = self.player[0].init_BG_delay

        # if self.is_key_pressed(K_q): #BG_CHANGE_FOR_PRACTICUM
        #     MainGame.BG = MainGame.BLACK
        #     MainGame.BG_for_player = 1
        # else:
        #     MainGame.BG =  MainGame.WHITE
        #     MainGame.BG_for_player = 0

        self.player[0].check_offscreen()
        self.player[0].player_delay()
        self.player[0].check_endgame()
        self.player[0].player_check_color(MainGame.BG_for_player)

        if self.player[0].delay <= 0:
            if self.is_key_pressed(K_w) or self.get_switch('up', 0):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,0,-75) ):
                            collide = True
                if not collide:
                    self.player[0].move_up()

            elif self.is_key_pressed(K_s) or self.get_switch('down', 0):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,0,+75) ):
                            collide = True
                if not collide:
                    self.player[0].move_down()

            elif self.is_key_pressed(K_a) or self.get_switch('left', 0):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,-75,0) ):
                            collide = True
                if not collide:
                    self.player[0].move_left()
            elif self.is_key_pressed(K_d) or self.get_switch('right', 0):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[0].x,self.player[0].y,+75,0) ):
                            collide = True
                if not collide:
                    self.player[0].move_right() #movement
                self.player[0].check_offscreen() #P1

        self.player[1].check_offscreen()
        self.player[1].player_delay()
        self.player[1].check_endgame()
        self.player[1].player_check_color(MainGame.BG_for_player)

        if self.player[1].delay <= 0:
            if self.is_key_pressed(K_UP) or self.get_switch('up', 1):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,0,-75) ):
                            collide = True
                if not collide:
                    self.player[1].move_up()

            elif self.is_key_pressed(K_DOWN) or self.get_switch('down', 1):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,0,+75) ):
                            collide = True
                if not collide:
                    self.player[1].move_down()

            elif self.is_key_pressed(K_LEFT) or self.get_switch('left', 1):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,-75,0) ):
                            collide = True
                if not collide:
                    self.player[1].move_left()
            elif self.is_key_pressed(K_RIGHT) or self.get_switch('right', 1):
                collide = False
                for i in range(0,20,2):
                    for j in range(0,14,2):
                        if ( self.world_map[i][j].collision(self.player[1].x,self.player[1].y,+75,0) ):
                            collide = True
                if not collide:
                    self.player[1].move_right() #movement #P2

        for k in range(0,self.bomb_number,1): #bombloop

            self.bomb[k].check_blast_color(MainGame.blast_color_check)

            if (self.is_key_pressed(K_SPACE) or self.get_switch('bomb', 0) and not self.bomb[k].isPlant ) :
                self.bomb[k].plant_bomb(self.player[0].get_x(), self.player[0].get_y())

            self.bomb[k].bomb_decay()
            self.bomb[k].bomb_blast()
            for i in range(0,self.player_number,1):
                self.bomb[k].check_player(self.player[i]) #P1

        for k in range(0,self.bomb_number,1): #bombloop

            self.bomb2[k].check_blast_color(MainGame.blast_color_check)

            if (self.is_key_pressed(K_RCTRL) or self.get_switch('bomb', 1) and not self.bomb2[k].isPlant ) :
                self.bomb2[k].plant_bomb(self.player[1].get_x(), self.player[1].get_y())

            self.bomb2[k].bomb_decay()
            self.bomb2[k].bomb_blast()
            for i in range(0,self.player_number,1):
                self.bomb2[k].check_player(self.player[i]) #P2

        for i in range(0,20,2):
            for j in range(0,14,2):
                self.world_map[i][j].wall_random_position()
                self.world_map[i][j].check_wall_offscreen()



    def render(self, surface):
        for i in range(0,self.player_number,1):
            self.player[i].render(surface)
        for x in range(0,self.bomb_number,1):
            self.bomb[x].render(surface)
        for x in range(0,self.bomb_number,1):
            self.bomb2[x].render(surface)
        for i in range(0,20,2):
            for j in range(0,14,2):
                self.world_map[i][j].render(surface)

def main():
    game = MainGame()
    game.run()

if __name__ == '__main__':
    main()