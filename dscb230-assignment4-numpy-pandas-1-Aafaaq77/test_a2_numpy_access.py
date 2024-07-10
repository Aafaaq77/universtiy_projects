from a2_numpy_access import arr1, arr2, task2_stepwise, task2_masked_selection_sum

import numpy as np
import unittest
import pytest


class A2NumpyTest(unittest.TestCase):
    
    def setUp(self):
        pass

    # pytest test_a2_numpy_access.py -k "test_task2_stepwise" 
    def test_task2_stepwise(self): # 5 Punkte
        a1 = task2_stepwise(arr1)
        np.testing.assert_array_equal(a1, np.array([[2., 8., 5.],[2., 6., 3.],[5., 9., 1.],[1., 5., 6.],[1., 4., 7.]]))

        a2 = task2_stepwise(arr2)
        np.testing.assert_array_equal(a2, np.array([[7., 4., 5.],[4., 2., 8.],[8., 8., 2.],[2., 5., 4.],[8., 6., 5.]]))

    
    # pytest test_a2_numpy_access.py -k "test_task2_masked_selection_sum" 
    def test_task2_masked_selection_sum(self): # 30 Punkte
        sum1 = task2_masked_selection_sum(arr1)
        self.assertEqual(sum1, 331.0)
        
        sum2 = task2_masked_selection_sum(arr2)
        self.assertEqual(sum2, 341.0)

        sum3 = task2_masked_selection_sum(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
        self.assertEqual(sum3, 42.0)

        sum4 = task2_masked_selection_sum(np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[1,10,2,20]]))
        self.assertEqual(sum4, 84.0)

        

    
if __name__ == '__main__':
    unittest.main()

