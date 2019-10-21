'''
Jael Butler and Mitchell Walker
CS 4820
December 09 2019

This module holds all of the functions and methods for creating and solving an
arbitrary sized Rubik's cube.

We assume that:
    Blue is the front face
    Green is the back
    White is the right
    Yellow is the left
    Red is the top
    Orange is the bottom
You can change this by changing the character values in the initialization.

Note that rows are 0 to n-1, top down.
          cols are 0 to n-1, left right.
          depths are 0 to n-1 front back.
'''

from random import randint
import numpy as np


class Cube:
    def __init__(self, n, front='B', back='G', left='Y', right='W', top='R', bottom='O'):
        self.n = n
        self.front_face = np.full((n,n), front)
        self.back_face = np.full((n,n), back)
        self.right_face = np.full((n,n), right)
        self.left_face = np.full((n,n), left)
        self.top_face = np.full((n,n), top)
        self.bottom_face = np.full((n,n), bottom)

        self.directions = [1,-1]
        self.rotation_methods = [self.rotate_row, self.rotate_column, self.rotate_layer]

        self.max_rotations = 0

    def set_faces(self, faces):
        self.front_face = faces[0]
        self.back_face = faces[1]
        self.left_face = faces[2]
        self.right_face = faces[3]
        self.top_face = faces[4]
        self.bottom_face = faces[5]


    # Shuffles the cube for r rotations.
    def shuffle_cube(self, rotations):
        for i in range(0, rotations):
            index = randint(0,self.n-1)
            dir_index = randint(0,1)
            rot_index = randint(0,2)
            rotation_method = self.rotation_methods[rot_index]
            rotation_method(index, self.directions[dir_index])
            max_rotations = rotations


    # Rotates a row (horizontally, x), 1 is right, and -1 is left.
    def rotate_row(self, row, direction):
        rows = np.append(self.front_face[row], [self.left_face[row], self.back_face[row], self.right_face[row]])
        rows = np.roll(rows, direction*self.n)
        (self.front_face[row], self.left_face[row], self.back_face[row], self.right_face[row]) = np.split(rows, 4)


    # Rotates a column (vertically, y) (1 backwards and -1 is forwards)
    def rotate_column(self, col, direction):
        cols = np.append(self.front_face[:,col], [self.top_face[:,col], self.back_face[:,col], self.bottom_face[:,col]])
        cols = np.roll(cols, direction*self.n)
        (self.front_face[:,col], self.top_face[:,col], self.back_face[:,col], self.bottom_face[:,col]) = np.split(cols, 4)


    # Rotate a depth layer (z) (1 counterclockwise, -1 clockwise)
    # Note that depth corresponds to a row on some faces and columns on others.
    def rotate_layer(self, depth, direction):
        depths = np.append(self.top_face[-depth-1], [self.left_face[:,-depth-1], self.bottom_face[depth], self.right_face[:,depth]])
        depths = np.roll(depths, direction*self.n)
        (self.top_face[-depth-1], self.left_face[:,-depth-1], self.bottom_face[depth], self.right_face[:,depth]) = np.split(depths, 4)

    def print_cube(self):
        print ("Front:\n", self.front_face)
        print ("Back:\n", self.back_face)
        print ("Left:\n", self.left_face)
        print ("Right:\n", self.right_face)
        print ("Top:\n", self.top_face)
        print ("Bottom:\n", self.bottom_face)
