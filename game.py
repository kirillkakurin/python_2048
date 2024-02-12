import pygame as pg
from main import *

class _2048():
    def __init__(self, x, y):
        self.rect = self.get_rect(
            bottomleft=(x,y))
        self.speed_y = 0
        self.speed_x = 0
        self.phase = 0

    def move(self, speed, tiles_h, tiles_w):
        self.phase -= 1
        self.speed_y += speed
        self.rect.y += H + tile_center_h