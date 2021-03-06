import pygame
import sys
import Vector

class Player():
    def __init__(self, team, r = 12, x = 20, y = 20, vx = 1, vy = 1, a = 300, color = (245,234,213)):
        self.color = color
        self.r = r
        self.a =a
        self._team = team
        self.keys1 = (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s)
        self.score = 0
        self.weight = 30
        self.speed = Vector.Vector(vx,vy)
        self.pos = Vector.Vector(x,y)

    def render(self,game):
        color = [(230,51,51),(54,116,225)]
        position = (int(self.pos.x),int(self.pos.y))
        """Draw Player on the Game window"""
        Object = game.font.render(str(self.score), True,color[self._team])
        game.screen.blit(Object,(game.width-100,game.height/2 + (self._team-1)*100))
        pygame.draw.circle(game.screen,self.color,position,self.r)

    def update(self,game):
        """Update Player state"""
        if game.pressed[self.keys1[self._team*4]]:
            self.speed -= Vector.Vector(1,0) * game.delta * self.a
            #self.x-=game.delta * self.a
        if game.pressed[self.keys1[self._team*4+1]]:
            self.speed += Vector.Vector(1,0) * game.delta * self.a
            #self.x+=game.delta * self.a
        if game.pressed[self.keys1[self._team*4+2]]:
            self.speed -= Vector.Vector(0,1) * game.delta * self.a
            #self.y-=game.delta * self.a
        if game.pressed[self.keys1[self._team*4+3]]:
            self.speed += Vector.Vector(0,1) * game.delta * self.a
            #self.y+=game.delta * self.a
        if (game.mode == 1):
            self.speed -= self.speed * game.delta
            self.pos += self.speed * game.delta

        """Do not let Player get out of the Game window"""
        """Касание левой грани"""
        if self.pos.x-self.r-game.ethik < 0:
            if self.speed.x != 0:
                self.speed.x = 0
            self.pos.x = self.r + game.ethik

        """Касание верхней грани"""
        if self.pos.y < self._team*(game.height/2) + (self.r) - (self._team-1)*(game.ethik):
            if self.speed.y != 0:
                self.speed.y = 0
            self.pos.y = self._team*(game.height/2) + (self.r) - (self._team-1)*(game.ethik)

        """Касание правой грани"""
        if self.pos.x > game.width - self.r - game.ethik:
            if self.speed.x != 0:
                self.speed.x = 0
            self.pos.x = game.width - self.r - game.ethik

        """Касание нижней грани"""
        if self.pos.y > (self._team+1)*game.height/2 - self.r - (self._team)*(game.ethik):
            if self.speed.y != 0:
                self.speed.y = 0
            self.pos.y = (self._team+1)*game.height/2 - self.r - (self._team)*(game.ethik)

    def start_pos(self,game):
        self.pos = Vector.Vector(game.width/2,(game.height-self.r*2)*self._team + abs(self._team-1)*self.r*2)
        self.speed = Vector.Vector(0,0)

