from task1_category_analysis import task1_category_vendor_sales, task1_category_item_ranking_top3

import pandas as pd
import numpy as np
import unittest
import pytest


class Task1PandasTest(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_parquet("Iowa_Liquor_Sales2020-21.parquet")

    # pytest test_task1_category_analysis.py -k "test_task1_category_vendor_sales" 
    def test_task1_category_vendor_sales(self): # 10 Punkte
        res = task1_category_vendor_sales(self.df)
        self.assertEqual(res.shape, (824,1) )
        self.assertAlmostEqual(res.iloc[0,0], 1684653.70)
        self.assertAlmostEqual(res.iloc[-1,0], 6.75)
        
        res = task1_category_vendor_sales(self.df.sample(int(0.5*len(self.df)), random_state=0))
        self.assertEqual(res.shape, (742,1) )
        self.assertAlmostEqual(res.iloc[0,0], 917452.40)
        self.assertAlmostEqual(res.iloc[-1,0], 6.56)


        res = task1_category_vendor_sales(self.df.sample(int(0.2*len(self.df)), random_state=1))
        self.assertEqual(res.shape, (649,1) )
        self.assertAlmostEqual(res.iloc[0,0], 393334.09)
        self.assertAlmostEqual(res.iloc[-1,0], 10.8)


    # pytest test_task1_category_analysis.py -k "test_task1_category_item_ranking_top3" 
    def test_task1_category_item_ranking_top3(self): # 20 Punkte
        res = task1_category_item_ranking_top3(self.df)
        
        self.assertEqual(res.shape, (153,4) )
        self.assertAlmostEqual(res.iloc[0,-2], 1663245.70)
        self.assertEqual(res.iloc[-1,1], 'Big Peach Liqueur')
        
        res = task1_category_item_ranking_top3(self.df.sample(int(0.5*len(self.df)), random_state=0))
        self.assertEqual(res.shape, (146,4) )
        self.assertAlmostEqual(res.iloc[0,-2], 908678.00)
        self.assertEqual(res.iloc[-1,1], 'Mr. Boston Sloe Gin')


        res = task1_category_item_ranking_top3(self.df.sample(int(0.2*len(self.df)), random_state=1))
        self.assertEqual(res.shape, (142,4) )
        self.assertAlmostEqual(res.iloc[0,-2], 389532.49)
        self.assertEqual(res.iloc[-4,1], 'Paramount Sloe Gin')
        
    
if __name__ == '__main__':
    unittest.main()

