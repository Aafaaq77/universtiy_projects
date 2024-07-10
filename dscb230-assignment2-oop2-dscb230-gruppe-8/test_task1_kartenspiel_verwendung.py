from kartenspiel import Spielkarte, Kartenspiel
from kartenspiel_verwendung import create_random_spielkarte, create_doppelkopf
import unittest
import pytest


class KartenspielVerwendungTest(unittest.TestCase):
    
    def setUp(self):
        pass
       
    # pytest test_task1_kartenspiel_verwendung.py -k "test_task1_random_spielkarte_method" 
    def test_task1_random_spielkarte_method(self): # 5 Punkte
        # erzeuge vier zufällige Spielkarten über die Methode - mindestens eine sollte sich von den anderen unterscheiden
        k1 = create_random_spielkarte()
        k2 = create_random_spielkarte()
        k3 = create_random_spielkarte()
        k4 = create_random_spielkarte()
        
        self.assertTrue(k1 != k2 or k1 != k3 or k1 != k4 or k2 != k3 or k2 != k4 or k3 != k4, msg="Zufällige Kartenerzeugung in Methode create_random_spielkarte funktioniert nicht.")


    # pytest test_task1_kartenspiel_verwendung.py -k "test_task1_random_spielkarte_constructor" 
    def test_task1_random_spielkarte_constructor(self): # 5 Punkte
        # erzeuge vier zufällige Spielkarten über den Konstruktor - mindestens eine sollte sich von den anderen unterscheiden
        k1 = Spielkarte()
        k2 = Spielkarte()
        k3 = Spielkarte()
        k4 = Spielkarte()
        
        self.assertTrue(k1 != k2 or k1 != k3 or k1 != k4 or k2 != k3 or k2 != k4 or k3 != k4, msg="Zufällige Kartenerzeugung im Konstruktor funktioniert nicht.")

    # pytest test_task1_kartenspiel_verwendung.py -k "test_task1_doppelkopf" 
    def test_task1_doppelkopf(self): # 10 Punkte
        # testet, ob alle Karten zweimal vorkommen
        dk = create_doppelkopf()
        self.assertEqual(len(dk), 104, 'Kartenspiel hat nicht 104 Karten (vom Doppelkopf)')

        fw_count = {}
        
        for k in dk:
            if (k.farbe, k.wert) in fw_count.keys():
                fw_count[(k.farbe, k.wert)] += 1
            else:
                fw_count[(k.farbe, k.wert)] = 1
            
        self.assertEqual(set(fw_count.values()), {2}, msg="Nicht alle Karten kommen genau zweimal vor!")


    
if __name__ == '__main__':
    unittest.main()

