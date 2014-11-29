import pygame
from pygame.locals import *
from gamelib import SimpleGame

#########################################
class Player(object):
    player_white=pygame.image.load("Player_.png")
    player_black=pygame.image.load("Player_black.png")
    which_player = 1

    def __init__(self, radius, color, pos):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color
        self.delay = 1
        self.this_player = Player.which_player
        Player.which_player += 1

    def player_move_delay(self):
        self.delay -= (0.1)


    def move_up(self):
            self.y = self.y-75
            self.delay = 1
            #print self.x,self.y

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
    bomb_image = []
    def __init__(self):

        self.blast_range = 214
        self.blast_position = 94

        self.blast_color = pygame.Color('white')

        self.bomb_position = (SimpleGame.Resolution_X+1000,SimpleGame.Resolution_Y+1000)
        (self.x,self.y) = self.bomb_position

        self.time = 8
        self.isPlant = False
        self.isBomb = False
        self.blastTime = 3


    def check_blast_color(self,color):
        if(color is 0):
            self.blast_color = pygame.Color('black')
            Bomb.bomb_image = pygame.image.load("bBomb.png")
        elif(color is 1):
            self.blast_color = pygame.Color('white')
            Bomb.bomb_image = pygame.image.load("Bomb.png")


    def plant_bomb(self, x, y):
        self.bomb_position = (x+15,y+15)
        self.isPlant = True


    def bomb_blast(self):
        if(self.isBomb):
            self.blastTime -= 0.1
        if(self.blastTime < 0):
            self.isBomb = False
            self.isPlant = False
            self.blastTime = 3
    i = 0
    def check_player(self,player):
        if self.isBomb and ((( self.bomb_position[0]-self.blast_position<= player.x+64 <= self.bomb_position[0]-self.blast_position + self.blast_range) and ( self.bomb_position[1]-16 <= player.y+64 <= self.bomb_position[1]-16 + self.blast_range) )
            or
            (( self.bomb_position[0]-16 <= player.x+64 <= self.bomb_position[0]-16 + self.blast_range ) and ( self.bomb_position[1]-self.blast_position <= player.y+64 <= self.bomb_position[1]-self.blast_position + self.blast_range))):
            Bomb.i += 1
            print " Player",player.this_player," DIED", Bomb.i," times"


    def bomb_decay(self):
        if(self.isPlant):
            self.time -= (0.1)
        if(self.time < 0):
            self.time = 8
            self.isBomb = True

    def render(self, surface):
            if(self.isPlant and not self.isBomb):
                surface.blit(self.bomb_image, self.bomb_position)
            if(self.isBomb):

                    tempRect = pygame.Rect(self.bomb_position[0]-self.blast_position, self.bomb_position[1]-16, self.blast_range, 64)
                    pygame.draw.rect(surface, self.blast_color, tempRect ,1 )

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

