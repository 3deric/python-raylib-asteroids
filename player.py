from pyray import *
from raylib import *
from os.path import join
import math as m

class Player:
    def __init__(self):
        self.pos = Vector2(250,150)
        self.vel = Vector2(0,0)
        self.acc = 0.1
        self.rot_speed = 250.0
        self.rot = 0.0
        self.scale = 1.0
        self.player_texture = load_texture(join('assets', 'playerShip1_blue.png'))
        self.input = Vector2(0,0)

    def move(self, delta : float):
        self.input.x = int(IsKeyDown(KEY_D)) - int(IsKeyDown(KEY_A))
        self.input.y = int(IsKeyDown(KEY_W)) - int(IsKeyDown(KEY_S))
        self.rot += self.input.x * self.rot_speed * delta

        if self.input.y > 0:
            self.vel.x += m.cos(m.radians(self.rot - 90)) * self.input.y * self.acc
            self.vel.y += m.sin(m.radians(self.rot - 90)) * self.input.y * self.acc

        self.pos.x += self.vel.x *  delta
        self.pos.y += self.vel.y *  delta

        # self.vel.x = Lerp(self.vel.x, 0, delta)
        # self.vel.y = Lerp(self.vel.y, 0, delta)

    def draw(self):
        source_rec : Rectangle = Rectangle(0.0, 0.0, self.player_texture.width, self.player_texture.height)
        dest_rec :Rectangle =Rectangle(self.pos.x, self.pos.y, self.player_texture.width, self.player_texture.height)
        origin : Vector2 = (self.player_texture.width/2, self.player_texture.height/2)

        draw_texture_pro(self.player_texture, source_rec, dest_rec, origin, self.rot, WHITE)
