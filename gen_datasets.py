'''
Jael Butler
CS 4820
10/23/2019

This script generates all of the needed datasets and saves them to a binary file.
We generate 1000 instances for each shuffle count away from the goal for the training set.
And 10 instances of each shuffle count for the testing.
'''
from rubiks import Cube
import numpy as np


def create_set(sizes, iters, dir):
    for n in sizes:
        print("Generating set for size", n)
        file = dir + '/size_' + str(n) + '.npy'

        cube_arr = []
        for s in range(0,shuffles+1):
            for iter in range(0,iters):
                cube = Cube(n)
                cube.shuffle_cube(s)
                faces = [cube.front_face, cube.back_face, cube.left_face, cube.right_face, cube.top_face, cube.bottom_face]
                cube_arr.append(faces)

        np.save(file, cube_arr)

        # Ensure load.
        arr = np.load(file)
        print(arr)


#sizes = (2,3,4,5,6,7)
sizes = (2,3,4)
shuffles = 26

create_set(sizes, 1000, './training')
create_set(sizes, 10, './testing')
