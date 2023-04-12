import numpy as np
from math import sin, cos, tan, radians

screenWidth = 800
screenHeight = 450

darkBlue = (21, 37, 55)
lightPink = (217, 181, 157)

#def projection_matrix(d):
#    return np.array([[1, 0, 0, 0],
#                      [0, 1, 0, 0],
#                      [0, 0, 0, 0],
#                      [0, 0, 1/d, 1]])

def projection_matrix(d):
    return np.array([[1/((screenWidth/screenHeight)*tan(radians(d/2))), 0, 0, 0],
                      [0, 1/tan(radians(d/2)), 0, 0],
                      [0, 0, 100/(100-0.1), -100*0.1/(100-0.1)],
                      [0, 0, 1, 0]])

def rotation_matrix_x(fi):
    fi = radians(fi)
    return np.array([[1, 0, 0, 0],
                     [0, cos(fi), -sin(fi), 0],
                     [0, sin(fi), cos(fi), 0],
                     [0, 0, 0, 1]])

def rotation_matrix_y(fi):
    fi = radians(fi)
    return np.array([[cos(fi), 0, sin(fi), 0],
                     [0, 1, 0, 0],
                     [-sin(fi), 0, cos(fi), 0],
                     [0, 0, 0, 1]])

def rotation_matrix_z(fi):
    fi = radians(fi)
    return np.array([[cos(fi), -sin(fi), 0, 0],
                     [sin(fi), cos(fi), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def translation_matrix(tx, ty, tz):
    return np.array([[1, 0, 0, tx],
                     [0, 1, 0, ty],
                     [0, 0, 1, tz],
                     [0, 0, 0, 1]])


