import pygame as pg
from actionHandling import *
from sceneInitialization import *
from settings import *

pg.init()

screen = pg.display.set_mode([screenWidth, screenHeight])

initialize_cubes()

while True: 
    zoom = handle_controls()    
    screen.fill(darkBlue)
    draw_cubes(screen, zoom)
    
