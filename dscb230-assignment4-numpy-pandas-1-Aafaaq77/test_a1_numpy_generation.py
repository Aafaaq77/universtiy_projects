from a1_numpy_generation import task1_filled_2darray, task1_from_logic, task1_load_from_file, task1_multiplied_interpolated, solution_func

import numpy as np
import unittest
import pytest


class A1NumpyTest(unittest.TestCase):
    
    def setUp(self):
        pass

    # pytest test_a1_numpy_generation.py -k "test_task1_filled_2darray" 
    def test_task1_filled_2darray(self): # 5 Punkte
        a1 = task1_filled_2darray((2,3), 1)
        a2 = task1_filled_2darray((3,7), 2)
        a3 = task1_filled_2darray((2,3), 1, dtype=np.int)

        self.assertEqual(type(a1), np.ndarray)
        self.assertEqual(type(a2), np.ndarray)
        self.assertEqual(type(a3), np.ndarray)

        self.assertEqual(a1.shape, (2, 3))
        self.assertEqual(a2.shape, (3, 7))
        self.assertEqual(a3.shape, (2, 3))

        self.assertEqual(a1.sum(), 6)
        self.assertEqual(a2.sum(), 42)
        self.assertEqual(a3.sum(), 6)

        self.assertEqual(a3.dtype, np.int)

    # pytest test_a1_numpy_generation.py -k "test_task1_multiplied_interpolated" 
    def test_task1_multiplied_interpolated(self): # 5 Punkte
        a1 = task1_multiplied_interpolated(4, 40, 10)
        np.testing.assert_array_equal(a1, np.array([ 40.,  72.,  96., 112., 120., 120., 112.,  96.,  72.,  40.]))

        a2 = task1_multiplied_interpolated(5, 90, 12)
        np.testing.assert_array_almost_equal(a2, np.array([ 60., 140., 204.54545455, 253.63636364, 287.27272727, 305.45454545, 308.18181818, 295.45454545, 267.27272727, 223.63636364, 164.54545455,  90.]))
        

    # pytest test_a1_numpy_generation.py -k "test_task1_load_from_file" 
    def test_task1_load_from_file(self): # 10 Punkte
        a1 = task1_load_from_file("file1.txt")
        a2 = task1_load_from_file("file2.txt")
        a3 = task1_load_from_file("file3.txt")
        
        self.assertEqual(a1.shape, (20, 5))
        self.assertEqual(a2.shape, (20, 2))
        self.assertEqual(a3.shape, (20, 5))

        self.assertEqual(a1[0, 0], 5.)
        self.assertEqual(a1[-1, -1], 4.)
        self.assertEqual(a2[0, 0], 9.)
        self.assertEqual(a2[-1, -1], 7.)
        self.assertEqual(a3[0, 0], 1.)
        self.assertEqual(a3[-1, -1], 7.)


    # pytest test_a1_numpy_generation.py -k "test_task1_from_logic" 
    def test_task1_from_logic(self): # 15 Punkte

        a1 = task1_from_logic((3,4), lambda x, y: x)  # entspricht der Logik von "myfunc" aus dem Übungsblatt (Zeilenindex eintragen)
        np.testing.assert_array_equal(a1, np.array([[0., 0., 0., 0.], [1., 1., 1., 1.], [2., 2., 2., 2.]]))

        a2 = task1_from_logic((3,4), lambda x, y: y)  # Logik: Spaltenindex eintragen
        np.testing.assert_array_equal(a2, np.array([[0., 1., 2., 3.], [0., 1., 2., 3.], [0., 1., 2., 3.]]))

        a3 = task1_from_logic((3,4), lambda x, y: x+y)  # Logik: Spaltenindex+Zeilenindex eintragen
        np.testing.assert_array_equal(a3, np.array([[0., 1., 2., 3.], [1., 2., 3., 4.], [2., 3., 4., 5.]]))

        a4 = task1_from_logic((6,6), solution_func)
        np.testing.assert_array_equal(a4, np.array([[ 0.,  1.,  2.,  3.,  4.,  5.], [10., 11., 12., 13., 14., 15.], [20., 21., 22., 23., 24., 25.], [30., 31., 32., 33., 34., 35.], [40., 41., 42., 43., 44., 45.], [50., 51., 52., 53., 54., 55.]]))

        a4 = task1_from_logic((2,3), solution_func)
        np.testing.assert_array_equal(a4, np.array([[ 0.,  1.,  2.], [10., 11., 12.]]))
        


    
if __name__ == '__main__':
    unittest.main()

