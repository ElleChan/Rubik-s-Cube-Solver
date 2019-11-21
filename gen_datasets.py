'''
Jael Butler
CS 4820
10/23/2019


'''
from rubiks import Cube
import numpy as np
import csv

# Creates a dataset file.
def create_set(n, shuffles, count, split):
    print("Generating set for size", n)

    train_handle = open('./datasets/training/size'+str(n)+'.csv', 'w', newline='')
    test_handle = open('./datasets/testing/size'+str(n)+'.csv', 'w', newline='')
    train_writer = csv.writer(train_handle)
    test_writer = csv.writer(test_handle)

    cubes = {}
    for c in range(count):
        if c % 100 == 0:
            print("\t", c)          
        for s in range(0, shuffles+1):
            cube = Cube(n, 1, 2, 3, 4, 5, 6)            # Choose numbers for faces instead of colors
            cube.shuffle_cube(s)
            faces = cube.get_faces()
            row = tuple(np.stack(faces).flatten())

            # Get best fit.
            if row in cubes.keys():
                if cube.max_rotations < cubes[row]:
                    cubes[row] = cube.max_rotations
            else:
                cubes[row] = cube.max_rotations

    # Add solved cube.
    cube = Cube(n, 1,2,3,4,5,6)
    faces = cube.get_faces()
    row = tuple(np.stack(faces).flatten())
    cubes[row] = 0

    #  Split dataset.
    keys = list(cubes.keys())
    training_set = keys[(split-1):]
    testing_set = keys[-split:]


    # Write datasets.
    for tr_cube in training_set:
        output = list(tr_cube)
        output.append(cubes[tr_cube])
        train_writer.writerow(output)
    for tst_cube in testing_set:
        output = list(tst_cube)
        output.append(cubes[tst_cube])
        test_writer.writerow(output)

    # Close handle.
    train_handle.close()
    test_handle.close()

# Create training sets.
#create_set(2, 26, 1000, './training')
#create_set(3, 26, 1000, './training')
create_set(2, 30, 2000, 100)      # 12 is the max for rot 1.
#create_set(3, 26, 5, './datasets/size3.csv')