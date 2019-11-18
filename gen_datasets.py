'''
Jael Butler
CS 4820
10/23/2019


'''
from rubiks import Cube
import numpy as np
import csv

# Creates a dataset file.
def create_set(n, shuffles, count, dir):
    print("Generating set for size", n)
    f_name = dir + '/size_' + str(n) + '.csv'
    handle = open(f_name, 'w', newline='')
    writer = csv.writer(handle)

    cubes = {}
    for c in range(count):          
        for s in range(1, shuffles+1):
            cube = Cube(n, 1, 2, 3, 4, 5, 6)            # Choose numbers for faces instead of colors
            cube.shuffle_cube(s)
            faces = cube.get_faces()
            row = tuple(np.stack(faces).flatten())

            while row in cubes.keys():                # Avoid duplicate cubes.
                if cube.max_rotations < cubes[row]:
                    cubes[row] = cube.max_rotations
                cube = Cube(n, 1, 2, 3, 4, 5, 6)      
                cube.shuffle_cube(s)
                faces = cube.get_faces()
                row = tuple(np.stack(faces).flatten())

            cubes[row] = cube.max_rotations    
            output = list(row)
            output.append(cube.max_rotations)
            writer.writerow(output)

    # Add solved cube.
    cube = Cube(n, 1,2,3,4,5,6)
    faces = cube.get_faces()
    row = tuple(np.stack(faces).flatten())
    output = list(row)
    output.append(cube.max_rotations)
    writer.writerow(output)

    # Close handle.
    handle.close()

# Create training sets.
#create_set(2, 26, 1000, './training')
#create_set(3, 26, 1000, './training')
create_set(2, 26, 1, './training')
create_set(3, 26, 1, './training')

# Create testing sets.
#create_set(2, 26, 10, './testing')
#create_set(3, 26, 10, './testing')
create_set(2, 26, 1, './testing')
create_set(3, 26, 1, './testing')