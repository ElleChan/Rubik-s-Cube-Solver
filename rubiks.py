'''
Jael Butler and Mitchell Walker
CS 4820
December 09 2019

This module holds all of the functions and methods for creating and solving an
arbitrary sized Rubik's cube.

We assume that:
    Blue is the front face
    Green is the back
    Red is the right
    Orange is the left
    White is the top
    Yellow is the bottom
You can change this by changing the character values in the initialization.
Numerical values are also permitted.

Note that rows are 0 to n-1, top down.
          cols are 0 to n-1, left right.
          depths are 0 to n-1 front back.

To see the orientation of each face, hold the cub from the perspective of the front.
Spinning left to right, shows the proper orientiation of the front, right, back, and left faces.
For the top, the bottom row is the one touching the front edge. This keeps the depth definition consistent.
'''

from random import randint
import numpy as np


class Cube:
    def __init__(self, n, front='B', back='G', left='R', right='O', top='W', bottom='Y'):
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

    # Sets the faces of the cube.
    def set_faces(self, front, back, left, right, top, bottom):
        self.front_face = front
        self.back_face = back
        self.left_face = left
        self.right_face = right
        self.top_face = top
        self.bottom_face = bottom

    # Returns the faces of the cube.
    def get_faces(self):
        return [self.front_face, self.back_face, self.left_face, self.right_face, self.top_face, self.bottom_face]


    # Shuffles the cube for r rotations.
    def shuffle_cube(self, rotations):
        for i in range(0, rotations):
            index = randint(0,self.n-1)                             # Pick a row/col/layer number
            while self.n % 2 == 1 and index == self.n // 2:         # Can't rotate middle row/col/layer when n is odd.
                index = randint(0,self.n-1)
            dir_index = randint(0,1)                                # Pick a direction
            rot_index = randint(0,2)                                # Pick a row, col, or layer
            rotation_method = self.rotation_methods[rot_index]      
            rotation_method(index, self.directions[dir_index])      # Rotate.
            max_rotations = rotations


    # Rotates a row (horizontally, x), 1 is left, and -1 is right.
    def rotate_row(self, row, direction):
        rows = np.append(self.front_face[row], [self.left_face[row], self.back_face[row], self.right_face[row]])
        rows = np.roll(rows, direction*self.n)
        (self.front_face[row], self.left_face[row], self.back_face[row], self.right_face[row]) = np.split(rows, 4)

        if row == 0:
            self.top_face = np.rot90(self.top_face, -direction)     
        elif row == self.n - 1:
            self.bottom_face = np.rot90(self.bottom_face, direction)


    # Rotates a column (vertically, y) (1 forwards and -1 is backwards)
    def rotate_column(self, col, direction):
        cols = np.append(self.front_face[:,col], [np.flip(self.bottom_face[:,self.n-1-col]), np.flip(self.back_face[:,self.n-1-col]), self.top_face[:,col]])
        cols = np.roll(cols, direction*self.n)
        (self.front_face[:,col], self.bottom_face[:,self.n-1-col], self.back_face[:,self.n-1-col], self.top_face[:,col]) = np.split(cols, 4)
        self.bottom_face[:,self.n-1-col] = np.flip(self.bottom_face[:,self.n-1-col])
        self.back_face[:,self.n-1-col] = np.flip(self.back_face[:,self.n-1-col])

        if col == 0:
            self.left_face = np.rot90(self.left_face, -direction)
        elif col == self.n -1:
            self.right_face = np.rot90(self.right_face, direction)


    # Rotate a depth layer (z) (1 counterclockwise, -1 clockwise)
    # Note that depth corresponds to a row on some faces and columns on others.
    def rotate_layer(self, depth, direction):
        depths = np.append(self.top_face[-depth-1], [self.right_face[:,depth], self.bottom_face[-depth-1], np.flip(self.left_face[:,-depth-1])])
        depths = np.roll(depths, -direction*self.n)
        (self.top_face[-depth-1], self.right_face[:,depth], self.bottom_face[-depth-1], self.left_face[:,-depth-1]) = np.split(depths, 4)
        self.left_face[:,-depth-1] = np.flip(self.left_face[:,-depth-1])

        if depth == 0:
            self.front_face = np.rot90(self.front_face, direction)
        elif depth == self.n -1:
            self.back_face = np.rot90(self.back_face, -direction)


    def print_cube(self):
        print ("Front:\n", self.front_face)
        print ("Back:\n", self.back_face)
        print ("Left:\n", self.left_face)
        print ("Right:\n", self.right_face)
        print ("Top:\n", self.top_face)
        print ("Bottom:\n", self.bottom_face)
