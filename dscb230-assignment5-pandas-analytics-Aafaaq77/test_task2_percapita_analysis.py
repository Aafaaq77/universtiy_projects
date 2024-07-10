from task2_percapita_analysis import task2_sales_per_capita

import pandas as pd
import numpy as np
import unittest
import pytest


class Task1PandasTest(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_parquet("Iowa_Liquor_Sales2020-21.parquet")

    # pytest test_task2_percapita_analysis.py -k "test_task2_sales_per_capita" 
    def test_task2_sales_per_capita(self): # 30 Punkte
        res = task2_sales_per_capita(self.df)
        self.assertEqual(res.shape, (10,6) )
        self.assertEqual(res.iloc[0,0], 'Winterset')
        self.assertAlmostEqual(res.iloc[1,3], 1029)
        self.assertAlmostEqual(res.iloc[-1,-1], 10.995338, places=4)
        self.assertAlmostEqual(res.iloc[-2,-2], 180.360670, places=4)

        
        res = task2_sales_per_capita(self.df.sample(int(0.5*len(self.df)), random_state=0))
        self.assertEqual(res.shape, (10,6) )
        self.assertEqual(res.iloc[0,0], 'Winterset')
        self.assertAlmostEqual(res.iloc[1,3], 1029)
        self.assertAlmostEqual(res.iloc[-1,-1], 6.578561, places=4)
        self.assertAlmostEqual(res.iloc[-2,-2], 90.279759, places=4)


        res = task2_sales_per_capita(self.df.sample(int(0.2*len(self.df)), random_state=1))
        self.assertEqual(res.shape, (10,6) )
        self.assertEqual(res.iloc[0,0], 'Winterset')
        self.assertAlmostEqual(res.iloc[2,3], 135)
        self.assertAlmostEqual(res.iloc[-1,-1], 2.082249, places=4)
        self.assertAlmostEqual(res.iloc[-2,-2], 36.242991, places=4)


        
    
if __name__ == '__main__':
    unittest.main()

