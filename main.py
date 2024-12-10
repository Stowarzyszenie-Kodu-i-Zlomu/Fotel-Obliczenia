import numpy as np
#set positions of pistons (x,y values)
p1 = [0,10,0]
p2 = [-5,-5,0]
p3 = [5,-5,0]
#height of zero position
h0 = 50
#set pitch and roll values
pitch = 45
roll = 0


def rotation_matrix(pitch, roll):
    """Creates a rotation matrix for pitch and roll."""

    R_pitch = np.array([
        [1, 0, 0],
        [0, np.cos(pitch), -np.sin(pitch)],
        [0, np.sin(pitch), np.cos(pitch)]
    ])
    R_roll = np.array([
        [np.cos(roll), 0, np.sin(roll)],
        [0, 1, 0],
        [-np.sin(roll), 0, np.cos(roll)]
    ])
    return R_roll @ R_pitch

def point_to_vector(point):
    """convert point to vector, duh"""
    return np.array([
        [point[0]],
        [point[1]],
        [point[2]]
    ])

def vector_to_point(vector):
    return np.array([vector[0], vector[1], vector[2]])

def set_height(height_zero, vector):
     return height_zero + vector[2]

def rotation(p1, p2, p3, height_zero, pitch, roll,):
    #convert points to vectors
    v1 = point_to_vector(p1)
    v2 = point_to_vector(p2)
    v3 = point_to_vector(p3)
    #calculate rotation matrix
    R = rotation_matrix(pitch,roll)
    #rotate each vector
    v1 = R @ v1
    v2 = R @ v2
    v3 = R @ v3
    #get height of each piston
    h1 = set_height(height_zero,v1)
    h2 = set_height(height_zero,v2)
    h3 = set_height(height_zero,v3)
    height = [h1,h2,h3]

    return height

height = rotation(p1, p2, p3, h0, pitch, roll)
print(height)
