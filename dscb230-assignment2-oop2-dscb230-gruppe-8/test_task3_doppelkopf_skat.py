from kartenspiel import Spielkarte, Kartenspiel, Doppelkopf, Skat

import unittest
import pytest


class KartenstapelTest(unittest.TestCase):
    
    def setUp(self):
        pass
       
    # pytest test_task3_doppelkopf_skat.py -k "test_task3_doppelkopf" 
    def test_task3_doppelkopf(self): # 13 Punkte
        dk = Doppelkopf()
        self.assertEqual(len(dk), 104, msg="Nicht die korrekte Anzahl von Karten bei Doppelkopf")

        fw_count = {}
        
        for k in dk:
            if (k.farbe, k.wert) in fw_count.keys():
                fw_count[(k.farbe, k.wert)] += 1
            else:
                fw_count[(k.farbe, k.wert)] = 1
            
        self.assertEqual(set(fw_count.values()), {2}, msg="Nicht alle Karten kommen genau zweimal vor!")

    
    # pytest test_task3_doppelkopf_skat.py -k "test_task3_skat" 
    def test_task3_skat(self): # 12 Punkte
        skat = Skat()
        self.assertEqual(len(skat), 32, msg="Nicht die korrekte Anzahl von Karten bei Skat")

        skat_count = {}
        
        for k in skat:
            if (k.farbe, k.wert) in skat_count.keys():
                skat_count[(k.farbe, k.wert)] += 1
            else:
                skat_count[(k.farbe, k.wert)] = 1
            
        self.assertEqual(set(skat_count.values()), {1}, msg="Nicht alle Karten kommen genau einmal vor!")

        for f in ['kreuz', 'pik', 'karo', 'herz']:
            for w in [7, 8, 9, 10, 'bube', 'dame', 'koenig', 'as']:
                self.assertTrue((f, w) in skat_count.keys())



    

    
if __name__ == '__main__':
    unittest.main()

