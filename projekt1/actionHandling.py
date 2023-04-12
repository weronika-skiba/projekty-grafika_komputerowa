import pygame as pg
from sceneInitialization import *

zoom = 60

def handle_controls():

    global zoom

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    input_key = pg.key.get_pressed()
    if input_key[pg.K_i]:
        rotate_x(0.1)
    if input_key[pg.K_k]:
        rotate_x(-0.1)
    if input_key[pg.K_j]:
        rotate_y(0.1)
    if input_key[pg.K_l]:
        rotate_y(-0.1)
    if input_key[pg.K_u]:
        rotate_z(-0.1)
    if input_key[pg.K_o]:
        rotate_z(0.1)
    if input_key[pg.K_d]:
        translate(0.2, 0, 0)
    if input_key[pg.K_a]:
        translate(-0.2, 0, 0)
    if input_key[pg.K_w]:
        translate(0, 0.2, 0)
    if input_key[pg.K_s]:
        translate(0, -0.2, 0)
    if input_key[pg.K_r]:
        translate(0, 0, 0.2)
    if input_key[pg.K_f]:
        translate(0, 0, -0.2)   
    if input_key[pg.K_c]:
        zoom = zoom * 1.01
    if input_key[pg.K_v]:
        zoom = zoom * 0.99
    pg.display.update()
    return zoom