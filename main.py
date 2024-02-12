import pygame as pg
import sys
from game import *

pg.init()

#window size
W = 800
H = 800

#amount of tiles
tiles_w = 4
tiles_h = 4

speed = 10

#number coordinates
tile_center_w = (W // tiles_w) // 2
tile_center_h = (H // tiles_h) // 2

sc = pg.display.set_mode((W, H))

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (35, 115, 100)
line_color = (50, 50, 50)

#number font
my_font = pg.font.SysFont("Calibri", 75, bold = True)
#tile text
_2048 = my_font.render("2048", 1, WHITE)
_1024 = my_font.render("1024", 1, WHITE)
_512 = my_font.render("512", 1, WHITE)
_256 = my_font.render("256", 1, WHITE)
_128 = my_font.render("128", 1, WHITE)
_64 = my_font.render("64", 1, WHITE)
_32 = my_font.render("32", 1, WHITE)
_16 = my_font.render("16", 1, WHITE)
_8 = my_font.render("8", 1, WHITE)
_4 = my_font.render("4", 1, WHITE)
_2 = my_font.render("2", 1, WHITE)

#positions
tile_1_1 = 0 + tile_center_w, 0 + tile_center_h
tile_1_2 = W // 2 - tile_center_w, 0 + tile_center_h
tile_1_3 = W // 4 * 3 - tile_center_w, 0 + tile_center_h
tile_1_4 = W - tile_center_w, 0 + tile_center_h
tile_2_1 = 0 + tile_center_w, H // 4 + tile_center_h
tile_2_2 = W // 4 + tile_center_w, H // 4 + tile_center_h
tile_2_3 = W // 4 * 3 - tile_center_w, H // 2 - tile_center_h
tile_2_4 = W - tile_center_w, H // 2 - tile_center_h
tile_3_1 = 0 + tile_center_w, H // 2 + tile_center_h
tile_3_2 = W // 4 + tile_center_w, H // 2 + tile_center_h
tile_3_3 = W // 2 + tile_center_w, H // 2 + tile_center_h
tile_3_4 = W - tile_center_w, H // 4 * 3 - tile_center_h
tile_4_1 = 0 + tile_center_w, H // 4 * 3 + tile_center_h
tile_4_2 = W // 4 + tile_center_w, H // 4 * 3 + tile_center_h
tile_4_3 = W // 2 + tile_center_w, H // 4 * 3 + tile_center_h
tile_4_4 = W - tile_center_w, H // 4 * 3 + tile_center_h
def draw_borders():
    # borders and tile separators
    pg.draw.line(sc, line_color, (0, 0), (0, H), 10)
    pg.draw.line(sc, line_color, (W, 0), (W, H), 10)
    pg.draw.line(sc, line_color, (0, 0), (W, 0), 10)
    pg.draw.line(sc, line_color, (0, H), (W, H), 10)

    pg.draw.line(sc, line_color, (W // 4, 0), (W // 4, H), 10)
    pg.draw.line(sc, line_color, (W // 2, 0), (W // 2, H), 10)
    pg.draw.line(sc, line_color, (W // 4 * 3, 0), (W // 4 * 3, H), 10)

    pg.draw.line(sc, line_color, (0, H // 4), (W, H // 4), 10)
    pg.draw.line(sc, line_color, (0, H // 2), (W, H // 2), 10)
    pg.draw.line(sc, line_color, (0, H // 4 * 3), (W, H // 4 * 3), 10)

def display_numbers():
    # tile display
    _2048_rect = _2048.get_rect(center=(tile_4_1))
    sc.blit(_2048, _2048_rect)
    _1024_rect = _1024.get_rect(center=(tile_4_2))
    sc.blit(_1024, _1024_rect)
    _512_rect = _512.get_rect(center=(tile_3_1))
    sc.blit(_512, _512_rect)
    _256_rect = _256.get_rect(center=(tile_4_3))
    sc.blit(_256, _256_rect)
    _128_rect = _128.get_rect(center=(tile_3_2))
    sc.blit(_128, _128_rect)
    _64_rect = _64.get_rect(center=(tile_2_1))
    sc.blit(_64, _64_rect)
    _32_rect = _32.get_rect(center=(tile_3_3))
    sc.blit(_32, _32_rect)
    _16_rect = _16.get_rect(center=(tile_1_1))
    sc.blit(_16, _16_rect)
    _8_rect = _8.get_rect(center=(tile_4_4))
    sc.blit(_8, _8_rect)
    _4_rect = _4.get_rect(center=(tile_3_4))
    sc.blit(_4, _4_rect)
    _2_rect = _2.get_rect(center=(tile_2_2))
    sc.blit(_2, _2_rect)

while True:
    sc.fill(DARK_BLUE)

    draw_borders()
    display_numbers()

    keys = pg.key.get_pressed()
    if [pg.K_SPACE]:
        move(_2048)

    for i in pg.event.get():
        if i.type == pg.QUIT:
            # pygame.quit()
            sys.exit()

    pg.display.update()