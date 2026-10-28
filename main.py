from pyray import *
from raylib import *
from player import Player

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, 'Asteroids')

player = Player()

while not window_should_close():
    dt : float = get_frame_time()
    begin_drawing()
    clear_background(BLACK)

    draw_fps(10,10)
    player.move(dt)
    player.draw()

    end_drawing()

close_window()