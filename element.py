import pygame
from pygame.locals import *
from gamelib import SimpleGame


#########################################
class Player(object):
    player_white=pygame.image.load("Player_white.png")
    player_black=pygame.image.load("Player_black.png")

    def __init__(self, radius, color, pos):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color
        self.move_up_check = True
        self.move_down_check = True
        self.move_left_check = True
        self.move_right_check = True
        self.delay = 1

    def player_delay(self):
        self.delay -= (0.1)



    def move_up(self):

            self.y = self.y-75
            self.delay = 1
            # print self.x,self.y

    def move_down(self):

            self.y = self.y+75
            self.delay = 1
            # print self.x,self.y

    def move_left(self):

            self.x = self.x-75
            self.delay = 1
            # print self.x,self.y

    def move_right(self):

            self.x = self.x+75
            self.delay = 1
            # print self.x,self.y

    def check_move(self):
        if(self.y <= -10):
            self.y = 823
        if(self.y >= SimpleGame.Resolution_Y):
            self.y = 2
        if(self.x <= 0):
            self.x = 1207
        if(self.x >= SimpleGame.Resolution_X):
            self.x = 7

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y




    def render(self, surface):
        pos = (int(self.x),int(self.y))
        surface.blit(self.player_white, pos)


#########################################
class Bomb(object):
    bomb_image = pygame.image.load("Bomb.png")
    isbomb = True
    more_bomb_delay = 4
    delay = 7
    time = 8
    def __init__(self):
        self.time = Bomb.time
        self.plant_delay = Bomb.delay
        self.bomb_position = (SimpleGame.Resolution_X+1000,SimpleGame.Resolution_Y+1000)

    def plant_bomb(self, x, y):
        if(self.plant_delay <= 0 and Bomb.more_bomb_delay <= 0):
            Bomb.more_bomb_delay = 2
            self.isbomb = False
            self.time = Bomb.time
            self.plant_delay = Bomb.delay
            self.bomb_position = (x+15, y+15)
    def bomb_blast(self):
        if(self.time <= 0):
            self.isbomb = True
            #renderblast
    def blast_render(self):
        return 1

    def bomb_decay(self):
        self.time -= (0.1)
        self.plant_delay -= (0.1)
        Bomb.more_bomb_delay -= (0.1)

    def render(self, surface):
        if(self.isbomb is not True):
            surface.blit(self.bomb_image, self.bomb_position)

#########################################
class Wall(object):
    Wall_image = pygame.image.load("Wall.png")
    def __init__(self, pos, color):
        (self.x, self.y) = pos
        self.color = color
    def collision(self,player):
        if((player.x+64 > self.x) and(player.x < self.x+64) and (player.y+64 > self.y) and(player.y < self.y+64)):
            print self.x,self.y,"Hit"
    def render(self, surface):
        surface.blit(self.Wall_image, (self.x, self.y))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

