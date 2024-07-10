from task3_holiday_analysis import task3_holiday_analysis

import pandas as pd
import numpy as np
import unittest
import pytest


class Task1PandasTest(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.read_parquet("Iowa_Liquor_Sales2020-21.parquet")

    # pytest test_task3_holiday_analysis.py -k "test_task3_holiday_analysis" 
    def test_task3_holiday_analysis(self): # 40 Punkte
        res = task3_holiday_analysis(self.df)
        self.assertEqual(res.shape, (7,3) )
        self.assertEqual(res.iloc[0,0], 'Veterans Day')
        self.assertAlmostEqual(res.iloc[0,1], 157116.84, places=2)
        self.assertEqual(res.iloc[-1,-1], 2)
        self.assertAlmostEqual(res.iloc[-2,-2], 2549.28, places=2)
        
        res = task3_holiday_analysis(self.df.sample(int(0.5*len(self.df)), random_state=0))
        self.assertEqual(res.shape, (7,3) )
        self.assertEqual(res.iloc[0,0], 'Veterans Day')
        self.assertAlmostEqual(res.iloc[0,1], 71364.48, places=2)
        self.assertEqual(res.iloc[-1,-1], 2)
        self.assertAlmostEqual(res.iloc[-2,-2], 1362.66, places=2)        
        self.assertEqual(res[res.HolidayName=='Lincoln\'s Birthday'][('Sale (Dollars)', 'count')].iloc[0], 2)

        res = task3_holiday_analysis(self.df.sample(int(0.2*len(self.df)), random_state=1))
        self.assertEqual(res.shape, (7,3) )
        self.assertEqual(res.iloc[0,0], 'Veterans Day')
        self.assertAlmostEqual(res.iloc[0,1], 30007.44, places=2)
        self.assertEqual(res[res.HolidayName=='No Holiday'][('Sale (Dollars)', 'count')].iloc[0], 351)
        self.assertAlmostEqual(res.iloc[-2,-2],  502.62, places=2)   

       
       
    
if __name__ == '__main__':
    unittest.main()

