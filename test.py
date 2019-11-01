from rubiks import Cube
import numpy as np
import unittest

 
class Test(unittest.TestCase):
    # Ensure that rotating top row left changes cube correctly.
    def test_1(self):
        cube = Cube(3)
        front = np.array([['W','G','W'],['O','B','O'],['Y','B','Y']])
        right = np.array([['O','B','O'],['W','O','Y'],['O','G','O']])
        back = np.array([['W','B','W'],['R','G','R'],['Y','G','Y']])
        left = np.array([['R','G','R'],['W','R','Y'],['R','B','R']])
        top = np.array([['B','Y','B'],['O','W','R'],['G','Y','G']])
        bottom = np.array([['B','W','B'],['R','Y','O'],['G','W','G']])
        cube.set_faces(front, back, left, right, top, bottom)

        front = np.array([['O','B','O'],['O','B','O'],['Y','B','Y']])
        right = np.array([['W','B','W'],['W','O','Y'],['O','G','O']])
        back = np.array([['R','G','R'],['R','G','R'],['Y','G','Y']])
        left = np.array([['W','G','W'],['W','R','Y'],['R','B','R']])
        top = np.array([['G','O','B'],['Y','W','Y'],['G','R','B']])
        bottom = np.array([['B','W','B'],['R','Y','O'],['G','W','G']])
        cube.rotate_row(0, 1)

        np.testing.assert_array_equal(cube.get_faces(), [front,back,left,right,top,bottom], "Should be True")
    
    # Test rotating bottom row right.
    def test_2(self):
        cube = Cube(3)
        front = np.array([['W','G','W'],['O','B','O'],['Y','B','Y']])
        right = np.array([['O','B','O'],['W','O','Y'],['O','G','O']])
        back = np.array([['W','B','W'],['R','G','R'],['Y','G','Y']])
        left = np.array([['R','G','R'],['W','R','Y'],['R','B','R']])
        top = np.array([['B','Y','B'],['O','W','R'],['G','Y','G']])
        bottom = np.array([['B','W','B'],['R','Y','O'],['G','W','G']])
        cube.set_faces(front, back, left, right, top, bottom)

        front = np.array([['W','G','W'],['O','B','O'],['R','B','R']])
        right = np.array([['O','B','O'],['W','O','Y'],['Y','B','Y']])
        back = np.array([['W','B','W'],['R','G','R'],['O','G','O']])
        left = np.array([['R','G','R'],['W','R','Y'],['Y','G','Y']])
        top = np.array([['B','Y','B'],['O','W','R'],['G','Y','G']])
        bottom = np.array([['G','R','B'],['W','Y','W'],['G','O','B']])
        cube.rotate_row(2, -1)

        np.testing.assert_array_equal(cube.get_faces(), [front,back,left,right,top,bottom], "Should be True")

    # Test rotating left column forwards.
    def test_3(self):
        cube = Cube(3)
        front = np.array([['W','G','W'],['O','B','O'],['Y','B','Y']])
        right = np.array([['O','B','O'],['W','O','Y'],['O','G','O']])
        back = np.array([['W','B','W'],['R','G','R'],['Y','G','Y']])
        left = np.array([['R','G','R'],['W','R','Y'],['R','B','R']])
        top = np.array([['B','Y','B'],['O','W','R'],['G','Y','G']])
        bottom = np.array([['B','W','B'],['R','Y','O'],['G','W','G']])
        cube.set_faces(front, back, left, right, top, bottom)

        front = np.array([['B','G','W'],['O','B','O'],['G','B','Y']])
        right = np.array([['O','B','O'],['W','O','Y'],['O','G','O']])
        back = np.array([['W','B', 'B'],['R','G','O'],['Y','G','G']])
        left = np.array([['R','W','R'],['B','R','G'],['R','Y','R']])
        top = np.array([['Y','Y','B'],['R','W','R'],['W','Y','G']])
        bottom = np.array([['B','W','Y'],['R','Y','O'],['G','W','W']])
        cube.rotate_column(0, 1)

        np.testing.assert_array_equal(cube.get_faces(), [front,back,left,right,top,bottom], "Should be True")

    # Test rotating right column backwards.
    def test_4(self):
        cube=Cube(3)
        front = np.array([['W','G','W'],['O','B','O'],['Y','B','Y']])
        right = np.array([['O','B','O'],['W','O','Y'],['O','G','O']])
        back = np.array([['W','B','W'],['R','G','R'],['Y','G','Y']])
        left = np.array([['R','G','R'],['W','R','Y'],['R','B','R']])
        top = np.array([['B','Y','B'],['O','W','R'],['G','Y','G']])
        bottom = np.array([['B','W','B'],['R','Y','O'],['G','W','G']])
        cube.set_faces(front, back, left, right, top, bottom)

        front = np.array([['W','G','G'],['O','B','R'],['Y','B','B']])
        right = np.array([['O','W','O'],['G','O','B'],['O','Y','O']])
        back = np.array([['G','B','W'],['R','G','R'],['B','G','Y']])
        left = np.array([['R','G','R'],['W','R','Y'],['R','B','R']])
        top = np.array([['B','Y','W'],['O','W','O'],['G','Y','Y']])
        bottom = np.array([['W','W','B'],['R','Y','O'],['Y','W','G']])
        cube.rotate_column(2, -1)
        
        np.testing.assert_array_equal(cube.get_faces(), [front,back,left,right,top,bottom], "Should be True")

    # Test rotating front layer counterclockwise
    def test_5(self):
        cube=Cube(3)
        front = np.array([['W','R','O'],['O','B','Y'],['G','R','R']])
        right = np.array([['Y','R','W'],['G','O','G'],['B','W','B']])
        back = np.array([['G','O','R'],['O','G','Y'],['W','R','O']])
        left = np.array([['B','O','G'],['B','R','W'],['Y','W','Y']])
        top = np.array([['W','B','R'],['Y','W','B'],['O','Y','G']])
        bottom = np.array([['O','W','B'],['G','Y','B'],['Y','G','R']])
        cube.set_faces(front, back, left, right, top, bottom)

        front = np.array([['O','Y','R'],['R','B','R'],['W','O','G']])
        right = np.array([['Y','R','W'],['G','O','G'],['R','W','B']])
        back = np.array([['G','O','R'],['O','G','Y'],['W','R','O']])
        left = np.array([['B','O','G'],['B','R','Y'],['Y','W','O']])
        top = np.array([['W','B','R'],['Y','W','B'],['Y','G','B']])
        bottom = np.array([['O','W','B'],['G','Y','B'],['Y','W','G']])
        cube.rotate_layer(0, 1)

        np.testing.assert_array_equal(cube.get_faces(), [front,back,left,right,top,bottom], "Should be True")

    # Test rotating back layer clockwise.
    def test_6(self):
        cube=Cube(3)
        front = np.array([['W','R','O'],['O','B','Y'],['G','R','R']])
        right = np.array([['Y','R','W'],['G','O','G'],['B','W','B']])
        back = np.array([['G','O','R'],['O','G','Y'],['W','R','O']])
        left = np.array([['B','O','G'],['B','R','W'],['Y','W','Y']])
        top = np.array([['W','B','R'],['Y','W','B'],['O','Y','G']])
        bottom = np.array([['O','W','B'],['G','Y','B'],['Y','G','R']])
        cube.set_faces(front, back, left, right, top, bottom)

        front = np.array([['W','R','O'],['O','B','Y'],['G','R','R']])
        right = np.array([['Y','R','W'],['G','O','B'],['B','W','R']])
        back = np.array([['R','Y','O'],['O','G','R'],['G','O','W']])
        left = np.array([['B','O','G'],['W','R','W'],['O','W','Y']])
        top = np.array([['Y','B','B'],['Y','W','B'],['O','Y','G']])
        bottom = np.array([['W','G','B'],['G','Y','B'],['Y','G','R']])
        cube.rotate_layer(2, -1)


        np.testing.assert_array_equal(cube.get_faces(), [front,back,left,right,top,bottom], "Should be True")


if __name__ == '__main__':
    unittest.main()
 