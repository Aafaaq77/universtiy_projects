from bank import Konto, Girokonto, Sparbuch, Bausparkonto

import unittest
import pytest


class BankTest(unittest.TestCase):
    
    def setUp(self):
        pass

    # pytest test_task1_bank.py -k "test_task1_abstract" 
    def test_abstract(self): # 10 Punkte
        # Testet, ob die Klasse Konto nicht instanziiert werden kann (das ist dann korrekt!)
        with self.assertRaises(TypeError):
            k = Konto('Meier', 123456)
       
    # pytest test_task1_bank.py -k "test_task1_sparbuch_basic" 
    def test_sparbuch_basic(self): # 5 Punkte
        # Testet das Sparbuch auf Basisfunktionen
        ind_zinssatz = 0.125

        # Objekterzeugung und Standard-Zinssatz prüfen
        sb_standard_zinssatz = Sparbuch('Meier', 123456)
        self.assertEqual(str(sb_standard_zinssatz), 'Sparbuch (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(sb_standard_zinssatz.zinssatz_haben, Sparbuch.zinssatz_haben_standard)
        
        # Objekterzeugung und Individuell-Zinssatz prüfen
        sb_individuell_zinssatz = Sparbuch('Müller', 987654, zinssatz_haben=ind_zinssatz)
        self.assertEqual(str(sb_individuell_zinssatz), 'Sparbuch (Inhaber Müller, Kontonr. 987654, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(sb_individuell_zinssatz.zinssatz_haben, ind_zinssatz)

    # pytest test_task1_bank.py -k "test_task1_girokonto_basic" 
    def test_girokonto_basic(self): # 10 Punkte
        # Testet das Girokonto auf Basisfunktionen
        ind_zinssatz = 0.125

        # Objekterzeugung und Standard-Zinssatz prüfen
        gk_standard_zinssatz = Girokonto('Meier', 123456, -500)
        self.assertEqual(str(gk_standard_zinssatz), 'Girokonto (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(gk_standard_zinssatz.zinssatz_haben, Girokonto.zinssatz_haben_standard)
        self.assertEqual(gk_standard_zinssatz.zinssatz_soll, Girokonto.zinssatz_soll_standard)
        
        # Objekterzeugung und Individuell-Zinssatz prüfen (1)        
        gk_ind_zinssatz = Girokonto('Meier', 123456, -500, zinssatz_haben=ind_zinssatz)
        self.assertEqual(str(gk_ind_zinssatz), 'Girokonto (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(gk_ind_zinssatz.zinssatz_haben, ind_zinssatz)
        self.assertEqual(gk_ind_zinssatz.zinssatz_soll, Girokonto.zinssatz_soll_standard)


        # Objekterzeugung und Individuell-Zinssatz prüfen (2)
        gk_ind_zinssatz = Girokonto('Meier', 123456, -500, zinssatz_soll=ind_zinssatz)
        self.assertEqual(str(gk_ind_zinssatz), 'Girokonto (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(gk_ind_zinssatz.zinssatz_haben, Girokonto.zinssatz_haben_standard)
        self.assertEqual(gk_ind_zinssatz.zinssatz_soll, ind_zinssatz)

        # Objekterzeugung und Individuell-Zinssatz prüfen (3)
        gk_ind_zinssatz = Girokonto('Meier', 123456, -500, zinssatz_haben=ind_zinssatz, zinssatz_soll=ind_zinssatz)
        self.assertEqual(str(gk_ind_zinssatz), 'Girokonto (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(gk_ind_zinssatz.zinssatz_haben, ind_zinssatz)
        self.assertEqual(gk_ind_zinssatz.zinssatz_soll, ind_zinssatz)


    # pytest test_task1_bank.py -k "test_task1_bausparkonto_basic" 
    def test_bausparkonto_basic(self): # 5 Punkte
        # Testet das Bausparkonto auf Basisfunktionen
        ind_zinssatz = 0.125

        # Objekterzeugung und Standard-Zinssatz prüfen
        bk_standard_zinssatz = Bausparkonto('Meier', 123456, 20000)
        self.assertEqual(str(bk_standard_zinssatz), 'Bausparkonto (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(bk_standard_zinssatz.zinssatz_haben, Bausparkonto.zinssatz_haben_standard)


        # Objekterzeugung und Individuell-Zinssatz prüfen (3)
        bk_ind_zinssatz = Bausparkonto('Meier', 123456, 20000, zinssatz_haben=ind_zinssatz)
        self.assertEqual(str(bk_ind_zinssatz), 'Bausparkonto (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        self.assertEqual(bk_ind_zinssatz.zinssatz_haben, ind_zinssatz)        




    # pytest test_task1_bank.py -k "test_task1_bank_rename" 
    def test_bank_rename(self): # 10 Punkte
        # Testet das Umbenennen von der Bank als statische Variable
        self.assertEqual(Konto.bankname, 'SPK')

        # Sparbuch
        sb = Sparbuch('Meier', 123456)
        self.assertEqual(str(sb), 'Sparbuch (Inhaber Meier, Kontonr. 123456, Bank SPK) mit Kontostand 0.0')
        
        # Girokonto
        gk = Girokonto('Müller', 987654, -500)
        self.assertEqual(str(gk), 'Girokonto (Inhaber Müller, Kontonr. 987654, Bank SPK) mit Kontostand 0.0')
        
        # Bausparkonto
        bk = Bausparkonto('Müller', 987654, -500)
        self.assertEqual(str(bk), 'Bausparkonto (Inhaber Müller, Kontonr. 987654, Bank SPK) mit Kontostand 0.0')

        Konto.aendere_bankname('SPK-KA')
        self.assertEqual(Konto.bankname, 'SPK-KA')
        self.assertEqual(str(sb), 'Sparbuch (Inhaber Meier, Kontonr. 123456, Bank SPK-KA) mit Kontostand 0.0')
        self.assertEqual(str(gk), 'Girokonto (Inhaber Müller, Kontonr. 987654, Bank SPK-KA) mit Kontostand 0.0')
        self.assertEqual(str(bk), 'Bausparkonto (Inhaber Müller, Kontonr. 987654, Bank SPK-KA) mit Kontostand 0.0')

        Konto.aendere_bankname('SPK')  # reset to default
        self.assertEqual(Konto.bankname, 'SPK')


    # pytest test_task1_bank.py -k "test_task1_bank_einzahlen" 
    def test_bank_einzahlen(self): # 10 Punkte
        # Testet das Einzahlen auf Konten
        sb = Sparbuch('Meier', 123456)
        gk = Girokonto('Müller', 987654, -500)
        bk = Bausparkonto('Müller', 987654, 20000)
        
        # Sparbuch
        betrag = 100.0
        self.assertEqual(sb.kontostand, 0.0)
        sb.einzahlen(betrag)
        self.assertEqual(sb.kontostand, betrag)

        # Girokonto
        self.assertEqual(gk.kontostand, 0.0)
        gk.einzahlen(betrag)
        self.assertEqual(gk.kontostand, betrag)

        # Bausparkonto
        self.assertEqual(bk.kontostand, 0.0)
        bk.einzahlen(betrag)
        self.assertEqual(bk.kontostand, betrag)        


    # pytest test_task1_bank.py -k "test_task1_bank_auszahlen_valide" 
    def test_bank_auszahlen_valide(self): # 10 Punkte
        # Testet valide Auszahlungen von Konten
        sb = Sparbuch('Meier', 123456)
        gk = Girokonto('Müller', 987654, -500)
        bk = Bausparkonto('Müller', 987654, 20000)
        
        einzahl_betrag = 500.0
        auszahl_betrag = 100.0
        
        # Sparbuch
        self.assertEqual(sb.kontostand, 0.0)
        sb.einzahlen(einzahl_betrag)
        self.assertEqual(sb.kontostand, einzahl_betrag)
        self.assertEqual(sb.auszahlen(auszahl_betrag), True)
        self.assertEqual(sb.kontostand, einzahl_betrag - auszahl_betrag)
        self.assertEqual(sb.auszahlen(auszahl_betrag), True)
        self.assertEqual(sb.kontostand, einzahl_betrag - 2*auszahl_betrag)

        # Girokonto
        self.assertEqual(gk.kontostand, 0.0)
        gk.einzahlen(einzahl_betrag)
        self.assertEqual(gk.kontostand, einzahl_betrag)
        self.assertEqual(gk.auszahlen(auszahl_betrag), True)
        self.assertEqual(gk.kontostand, einzahl_betrag - auszahl_betrag)
        self.assertEqual(gk.auszahlen(auszahl_betrag), True)
        self.assertEqual(gk.kontostand, einzahl_betrag - 2*auszahl_betrag)
        self.assertEqual(gk.auszahlen(auszahl_betrag*5), True)
        self.assertEqual(gk.kontostand, einzahl_betrag - 7*auszahl_betrag)  # überziehen möglich

        # Bausparkonto
        self.assertEqual(bk.kontostand, 0.0)
        bk.einzahlen(100*einzahl_betrag)
        self.assertEqual(bk.kontostand, 100*einzahl_betrag)
        self.assertEqual(bk.auszahlen(auszahl_betrag), True)  # Zuteilung erreicht
        


    # pytest test_task1_bank.py -k "test_task1_bank_auszahlen_nicht_valide" 
    def test_bank_auszahlen_nicht_valide(self): # 20 Punkte
        # Testet valide Auszahlungen von Konten
        sb = Sparbuch('Meier', 123456)
        gk = Girokonto('Müller', 987654, -500)
        bk = Bausparkonto('Müller', 987654, 20000)
        
        einzahl_betrag = 50.0
        auszahl_betrag = 600.0
        
        # Sparbuch
        self.assertEqual(sb.kontostand, 0.0)
        sb.einzahlen(einzahl_betrag)
        self.assertEqual(sb.kontostand, einzahl_betrag)
        self.assertEqual(sb.auszahlen(auszahl_betrag), False)  # würde unter 0 fallen
        self.assertEqual(sb.kontostand, einzahl_betrag)
        
        # Girokonto
        self.assertEqual(gk.kontostand, 0.0)
        gk.einzahlen(einzahl_betrag)
        self.assertEqual(gk.kontostand, einzahl_betrag)
        self.assertEqual(gk.auszahlen(auszahl_betrag), False)
        self.assertEqual(gk.kontostand, einzahl_betrag)  # nicht genug Deckung

        # Bausparkonto
        self.assertEqual(bk.kontostand, 0.0)
        bk.einzahlen(einzahl_betrag * 15)  # Betrag würde ausreichen, aber Zuteilung noch nicht erreicht
        self.assertEqual(bk.kontostand, einzahl_betrag * 15)
        self.assertEqual(bk.auszahlen(auszahl_betrag), False)  # Zuteilung nicht erreicht, keine Auszahlung möglich
        self.assertEqual(bk.kontostand, einzahl_betrag * 15)
        

    # pytest test_task1_bank.py -k "test_task1_bank_kalkuliere_zinsen" 
    def test_bank_kalkuliere_zinsen(self): # 20 Punkte
        # Testet Zinskalkulation
        sb = Sparbuch('Meier', 123456)
        gk = Girokonto('Müller', 987654, -500)
        bk = Bausparkonto('Müller', 987654, 20000)
        
        einzahl_betrag = 200.0
        auszahl_betrag = 600.0
        
        # Sparbuch
        self.assertEqual(sb.kontostand, 0.0)
        sb.einzahlen(einzahl_betrag)
        self.assertEqual(sb.kontostand, einzahl_betrag)
        self.assertEqual(sb.kalkuliere_zinsen(), True)
        self.assertEqual(sb.kontostand, einzahl_betrag + einzahl_betrag * sb.zinssatz_haben)
        
        # Girokonto
        self.assertEqual(gk.kontostand, 0.0)
        gk.einzahlen(einzahl_betrag)
        self.assertEqual(gk.kontostand, einzahl_betrag)
        self.assertEqual(gk.kalkuliere_zinsen(), True)
        self.assertEqual(gk.kontostand, einzahl_betrag + einzahl_betrag * gk.zinssatz_haben)  # Haben-Zinsen
        gk.auszahlen(auszahl_betrag)
        self.assertEqual(gk.kontostand, einzahl_betrag + einzahl_betrag * gk.zinssatz_haben - auszahl_betrag)
        
        kontostand_vorher = einzahl_betrag + einzahl_betrag * gk.zinssatz_haben - auszahl_betrag
        self.assertEqual(gk.kalkuliere_zinsen(), True)
        self.assertEqual(gk.kontostand, kontostand_vorher + kontostand_vorher * gk.zinssatz_soll)        


        # Bausparkonto
        self.assertEqual(bk.kontostand, 0.0)
        bk.einzahlen(einzahl_betrag)
        self.assertEqual(bk.kontostand, einzahl_betrag)
        self.assertEqual(bk.kalkuliere_zinsen(), True)  # solange Zuteilung nicht erreicht wurde Zinsen berechnen
        self.assertEqual(bk.kontostand, einzahl_betrag + einzahl_betrag * bk.zinssatz_haben)
        bk.einzahlen(einzahl_betrag * 100)  # Zuteilung erreichen
        
        kontostand_vorher = einzahl_betrag + einzahl_betrag * bk.zinssatz_haben + einzahl_betrag * 100.0
        self.assertEqual(bk.kontostand, kontostand_vorher)
        self.assertEqual(bk.kalkuliere_zinsen(), False)  # Zuteilung erreicht --> keine Zinsen berechnen
        self.assertEqual(bk.kontostand, kontostand_vorher)

    
if __name__ == '__main__':
    unittest.main()

