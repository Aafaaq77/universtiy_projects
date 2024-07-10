from kartenspiel import Spielkarte, Kartenspiel
from kartenstapel import Kartenstapel

import unittest
import pytest


class KartenstapelTest(unittest.TestCase):
    
    def setUp(self):
        pass
       
    # pytest test_task2_kartenstapel.py -k "test_task2_constructor_empty" 
    def test_task2_constructor_empty(self): # 10 Punkte
        stapel = Kartenstapel()
        self.assertEqual(stapel.karten, [], msg="Kein leerer Stapel erzeugt oder get-Methode fehlt")


    # pytest test_task2_kartenstapel.py -k "test_task2_len" 
    def test_task2_len(self): # 3 Punkte
        stapel = Kartenstapel()
        self.assertEqual(len(stapel), 0, msg="Len-Methode fehlt / nicht korrekt")
        stapel.karten.append(Spielkarte())
        self.assertEqual(len(stapel), 1, msg="Len-Methode fehlt / nicht korrekt")
        stapel.karten.append(Spielkarte())
        self.assertEqual(len(stapel), 2, msg="Len-Methode fehlt / nicht korrekt")

    
    # pytest test_task2_kartenstapel.py -k "test_task2_str" 
    def test_task2_str(self): # 12 Punkte
        stapel = Kartenstapel()
        self.assertEqual(str(stapel), "Leerer Kartenstapel", msg="String-Repräsentation fehlt / nicht korrekt")
        stapel.karten.append(Spielkarte(farbe='herz', wert='10'))
        stapel.karten.append(Spielkarte(farbe='karo', wert='as'))
        self.assertEqual(str(stapel), "Kartenstapel mit 2 Karten (herz 10, karo as)", msg="String-Repräsentation fehlt / nicht korrekt")

    # pytest test_task2_kartenstapel.py -k "test_task2_auflegen_abheben" 
    def test_task2_auflegen_abheben(self): # 10 Punkte
        stapel = Kartenstapel()
        stapel.karte_auflegen(Spielkarte(farbe='herz', wert='10'))
        stapel.karte_auflegen(Spielkarte(farbe='pik', wert='as'))
        self.assertEqual(len(stapel.karten), 2, msg="karte_auflegen nicht korrekt")
        self.assertEqual(str(stapel), "Kartenstapel mit 2 Karten (herz 10, pik as)", msg="karte_auflegen nicht korrekt")
        self.assertEqual(str(stapel.oberste_karte_abheben()), "pik as", msg="oberste_karte_abheben nicht korrekt")
        self.assertEqual(str(stapel.oberste_karte_abheben()), "herz 10", msg="oberste_karte_abheben nicht korrekt")

    
    # pytest test_task2_kartenstapel.py -k "test_task2_zufallskarte_mischen" 
    def test_task2_zufallskarte_mischen(self): # 10 Punkte
        stapel = Kartenstapel()
        stapel.karte_auflegen(Spielkarte(farbe='karo', wert='10'))
        stapel.karte_auflegen(Spielkarte(farbe='pik', wert='10'))
        
        k1 = stapel.zufallskarte_ziehen()
        self.assertEqual(len(stapel), 1, msg="Zufallskarte nicht aus Stapel entfernt?")
        k2 = stapel.zufallskarte_ziehen()
        self.assertEqual(len(stapel), 0, msg="Zufallskarte nicht aus Stapel entfernt?")
        self.assertNotEqual(k1, k2)

        stapel1 = Kartenstapel()
        stapel1.karte_auflegen(Spielkarte(farbe='karo', wert='10'))
        stapel1.karte_auflegen(Spielkarte(farbe='pik', wert='10'))
        stapel1.karte_auflegen(Spielkarte(farbe='herz', wert='10'))
        stapel1.karte_auflegen(Spielkarte(farbe='kreuz', wert='10'))
        stapel1.karte_auflegen(Spielkarte(farbe='herz', wert='as'))
        stapel1.karte_auflegen(Spielkarte(farbe='pik', wert='as'))


        stapel2 = Kartenstapel()
        stapel2.karte_auflegen(Spielkarte(farbe='karo', wert='10'))
        stapel2.karte_auflegen(Spielkarte(farbe='pik', wert='10'))
        stapel2.karte_auflegen(Spielkarte(farbe='herz', wert='10'))
        stapel2.karte_auflegen(Spielkarte(farbe='kreuz', wert='10'))
        stapel2.karte_auflegen(Spielkarte(farbe='herz', wert='as'))
        stapel2.karte_auflegen(Spielkarte(farbe='pik', wert='as'))
        
        self.assertTrue(stapel1.karten == stapel2.karten)

        stapel1.mischen()

        self.assertTrue(stapel1.karten != stapel2.karten)

    # pytest test_task2_kartenstapel.py -k "test_task2_constructor_kartenspiel" 
    def test_task2_constructor_kartenspiel(self): # 10 Punkte
        stapel = Kartenstapel(Kartenspiel())
        self.assertEqual(len(stapel), 52, msg="Kartenspiel nicht korrekt auf den Stapel gelegt")
        self.assertEqual(stapel.oberste_karte_abheben(), Spielkarte("herz", "as"), msg="Kartenspiel nicht korrekt auf den Stapel gelegt")

        


    
if __name__ == '__main__':
    unittest.main()

