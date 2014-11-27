import pygame
from pygame.locals import *
from gamelib import SimpleGame

#########################################
class Player(object):
    player_white=pygame.image.load("Player_.png")
    player_black=pygame.image.load("Player_black.png")

    def __init__(self, radius, color, pos):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color
        self.delay = 1

    def player_move_delay(self):
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

    def check_offscreen(self):
        if(self.y <= -10):
            self.y = 760
        if(self.y >= SimpleGame.Resolution_Y-64):
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
        self.blast_range = 224
        self.blast_position = 94

        self.blast_color = pygame.Color('white')

        self.blast_delay = 11
        self.time = Bomb.time
        self.check_blast_x_collide = False
        self.check_blast_y_collide = False
        self.plant_delay = Bomb.delay
        self.bomb_position = (SimpleGame.Resolution_X+1000,SimpleGame.Resolution_Y+1000)
        (self.x,self.y) = self.bomb_position

    def check_blast_color(self,color):
        if(color is 0):
            self.blast_color = pygame.Color('black')
        elif(color is 1):
            self.blast_color = pygame.Color('white')


    def plant_bomb(self, x, y):
        if(self.plant_delay <= 0 and Bomb.more_bomb_delay <= 0):
            self.blast_delay = 11
            Bomb.more_bomb_delay = 2
            self.isbomb = False
            self.time = Bomb.time
            self.plant_delay = Bomb.delay
            self.bomb_position = (x+15, y+15)
            (self.x,self.y) = (x, y)
    def bomb_blast(self):
        if(self.time <= 0):
            self.isbomb = True
    def blast_render(self):
        return 1

    def bomb_decay(self):
        self.time -= (0.1)
        self.plant_delay -= (0.1)
        Bomb.more_bomb_delay -= (0.1)
        self.blast_delay -= (0.1)

    def render(self, surface):
        if(self.isbomb is not True):
            surface.blit(self.bomb_image, self.bomb_position)
        if((self.isbomb is True )and (self.blast_delay > 0)):
            if(self.check_blast_x_collide is False):
                tempRect = pygame.Rect(self.bomb_position[0]-self.blast_position, self.bomb_position[1]-16, self.blast_range, 64)
                pygame.draw.rect(surface, self.blast_color, tempRect ,1 )
            if(self.check_blast_y_collide is False):
                tempRect2 = pygame.Rect(self.bomb_position[0]-16, self.bomb_position[1]-self.blast_position, 64, self.blast_range)
                pygame.draw.rect(surface, self.blast_color, tempRect2 ,1 )

#########################################
class Wall(object):
    Wall_image = pygame.image.load("Wall.png")
    bWall_image = pygame.image.load("bWall.png")
    def __init__(self, pos, color):
        (self.x, self.y) = pos
        self.color = color
        if(color is 0):
            self.image = Wall.Wall_image
        elif(color is 1):
            self.image = Wall.bWall_image
    def collision(self,x,y,move_x,move_y):
        if((x+64+move_x > self.x) and(x+move_x < self.x+64)
            and (y+64+move_y > self.y) and(y+move_y < self.y+64)):
            # print self.x,self.y,"hit wall"
            return True
    def render(self, surface):

        surface.blit(self.image, (self.x, self.y))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

