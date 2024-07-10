from a3_pandas import task3_pandas

import pandas as pd

import unittest
import pytest


class A2NumpyTest(unittest.TestCase):
    
    def setUp(self):
        pass

    # pytest test_a3_pandas.py -k "test_task3_pandas" 
    def test_task3_pandas(self): # 30 Punkte
        df = task3_pandas()
        
        self.assertEqual(df.shape, (15, 9))
        self.assertEqual(df.loc[244, 'mpg'], 43.1)
        self.assertEqual(df.loc[244, 'origin'], 'europe')

        self.assertEqual(df.loc[383, 'mpg'], 38.0)
        self.assertEqual(df.loc[383, 'origin'], 'japan')

        s_grouped = df.groupby('origin').mpg.count()
        self.assertEqual(s_grouped['europe'], 2)
        self.assertEqual(s_grouped['japan'], 10)
        self.assertEqual(s_grouped['usa'], 3)
        

    
    
    
if __name__ == '__main__':
    unittest.main()

