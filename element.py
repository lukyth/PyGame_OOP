import pygame
from pygame.locals import *

class Ball(object):

    def __init__(self, radius, color, pos, speed=(100,0)):
        (self.x, self.y) = pos
        (self.vx, self.vy) = speed
        self.radius = radius
        self.color = color

    def bounce_player(self):
        self.vx = abs(self.vx) # bounce ball back

    def move(self, delta_t, display, player):
        global score, game_over
        self.x += self.vx*delta_t
        self.y += self.vy*delta_t

        # make ball bounce if hitting wall
        if self.x < self.radius:
            self.vx = abs(self.vx)
            game_over = True # game over when ball hits left wall
        if self.y < self.radius:
            self.vy = abs(self.vy)
        if self.x > display.get_width()-self.radius:
            self.vx = -abs(self.vx)
        if self.y > display.get_height()-self.radius:
            self.vy = -abs(self.vy)

    def render(self, surface):
        pos = (int(self.x),int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

#########################################
class Player(object):

    THICKNESS = 10

    def __init__(self, pos, color, width=100):
        self.width = width
        self.pos = pos
        self.color = color

    def can_hit(self, ball):
        return self.pos-self.width/2.0 < ball.y < self.pos+self.width/2.0 \
            and ball.x-ball.radius < self.THICKNESS

    def move_up(self):
        self.pos -= 5

    def move_down(self):
        self.pos += 5

    def render(self, surface):
        pygame.draw.rect(surface,
                         self.color,
                         pygame.Rect(0,
                                     self.pos - self.width/2.0,
                                     self.THICKNESS,
                                     self.width),
                         2)
