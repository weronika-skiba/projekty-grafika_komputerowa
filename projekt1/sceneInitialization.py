import pygame as pg
import numpy as np
from math import sqrt
from settings import *

cubes = []

def create_cube(start_x, start_y, start_z, edge):
    cube_vertices = []
    cube_vertices.append([start_x, start_y, start_z, 1])
    cube_vertices.append([start_x + edge, start_y, start_z, 1])
    cube_vertices.append([start_x, start_y + edge, start_z, 1])
    cube_vertices.append([start_x, start_y, start_z + edge, 1])
    cube_vertices.append([start_x + edge, start_y + edge, start_z + edge, 1])
    cube_vertices.append([start_x + edge, start_y  + edge, start_z, 1])
    cube_vertices.append([start_x, start_y + edge, start_z + edge, 1])
    cube_vertices.append([start_x + edge, start_y, start_z + edge, 1])
    return cube_vertices

def initialize_cubes():
    global cubes
    cubes = []
    cubes.append((create_cube(0, 0, 50, 20), lightPink))
    #cubes.append((create_cube(40, 0, 50, 20), lightPink))
    #cubes.append((create_cube(0, 40, 50, 20), lightPink))
    #cubes.append((create_cube(40, 40, 50, 20), lightPink))
    #cubes.append((create_cube(0, 0, 90, 20), lightPink))
    #cubes.append((create_cube(40, 0, 90, 20), lightPink))
    #cubes.append((create_cube(0, 40, 90, 20), lightPink))
    #cubes.append((create_cube(40, 40, 90, 20), lightPink))


#def translate_for_display(coords):
#        return (screenWidth/2 + coords[0], screenHeight/2 - coords[1])
def translate_for_display(coords):
      return (screenWidth/2 + coords[0]*screenWidth/2,screenHeight/2 - coords[1]*screenHeight/2)

def rotate_y(fi):
    for cube in cubes:
        for i in range(len(cube[0])):
            vertex = cube[0][i]
            cube[0][i] = tuple(np.matmul(rotation_matrix_y(fi), vertex))

def rotate_z(fi):
    for cube in cubes:
        for i in range(len(cube[0])):
            vertex = cube[0][i]
            cube[0][i] = tuple(np.matmul(rotation_matrix_z(fi), vertex))

def rotate_x(fi):
    for cube in cubes:
        for i in range(len(cube[0])):
            vertex = cube[0][i]
            cube[0][i] = tuple(np.matmul(rotation_matrix_x(fi), vertex))

def translate(dx, dy, dz):
    for cube in cubes:
        for i in range(len(cube[0])):
            vertex = cube[0][i]
            cube[0][i] = tuple(np.matmul(translation_matrix(dx, dy, dz), vertex))


def normalize(vertex):
    return [vertex[0]/vertex[3], vertex[1]/vertex[3], vertex[2]/vertex[3], 1]

def draw_lines(screen, cube, color):
    pg.draw.aaline(screen, color, translate_for_display(cube[0]), translate_for_display(cube[1]))
    pg.draw.aaline(screen, color, translate_for_display(cube[0]), translate_for_display(cube[2]))
    pg.draw.aaline(screen, color, translate_for_display(cube[0]), translate_for_display(cube[3]))
    pg.draw.aaline(screen, color, translate_for_display(cube[4]), translate_for_display(cube[5]))
    pg.draw.aaline(screen, color, translate_for_display(cube[4]), translate_for_display(cube[6]))
    pg.draw.aaline(screen, color, translate_for_display(cube[4]), translate_for_display(cube[7]))
    pg.draw.aaline(screen, color, translate_for_display(cube[2]), translate_for_display(cube[5]))
    pg.draw.aaline(screen, color, translate_for_display(cube[2]), translate_for_display(cube[6]))
    pg.draw.aaline(screen, color, translate_for_display(cube[7]), translate_for_display(cube[1]))
    pg.draw.aaline(screen, color, translate_for_display(cube[7]), translate_for_display(cube[3]))
    pg.draw.aaline(screen, color, translate_for_display(cube[3]), translate_for_display(cube[6]))
    pg.draw.aaline(screen, color, translate_for_display(cube[1]), translate_for_display(cube[5]))

def draw_cubes(screen, zoom):
    for cube in cubes:
        cube_reprezentation = []
        for vertex in cube[0]:
            vertex_n = normalize(np.matmul(projection_matrix(zoom), vertex))
            #vertex_n = np.matmul(projection_matrix(zoom), vertex)
            cube_reprezentation.append(vertex_n)
        draw_lines(screen, cube_reprezentation, cube[1])