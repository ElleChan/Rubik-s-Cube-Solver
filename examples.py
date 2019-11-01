from rubiks import cube
from numpy import np

'''
# Example to shuffle cube.
cube = Cube(3)
cube.print_cube()
cube.shuffle_cube(1)
print()
cube.print_cube()
'''

'''
# Example to load dataset and initialize cube.
arr =  np.load('./testing/size_2.npy')
faces1 = arr[0]
print(faces1)
cube = Cube(len(faces1[0]))
cube.set_faces(faces1)
cube.print_cube()
'''