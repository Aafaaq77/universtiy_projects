from kartenspiel import Spielkarte, Kartenspiel
import random

class Kartenstapel():
    """ Klasse zur Repräsentation eines Kartenstapels """

    def __init__(self, kartenspiel = None):
        """ Konstruktor: legt einen neuen (leeren) Kartenstapel an, wenn kein Kartenspiel übegeben wurde.
                         Ansonsten alle Karten des Kartenspiels auf den Kartenstapel legen.
        """
        self._karten = []
        if kartenspiel:
            self._karten = kartenspiel._spielkarten

    """ Get- und Set-Methode des Attributs Karten """
    @property
    def karten(self):
        return self._karten

    @karten.setter
    def karten(self, value):
        self._karten = value
    
    def __len__(self):
        """ Gibt die Anzahl der Karten des Kartenstapels zurück bei Aufruf von len() """
        return len(self._karten)

    def __str__(self):
        """ Gibt die Länge des Kartenstapels mit allen Karten, als String, zurück, wenn der Stapel nicht leer ist. """
        if not self._karten:
            return "Leerer Kartenstapel"
        text = f"Kartenstapel mit {len(self)} Karten ("
        for karte in self._karten:
            text += f"{karte}, "
        return text[:-2] + ")"

    def karte_auflegen(self, karte):
        """ Legt eine neue Karte auf den Stapel """
        return self.karten.append(karte)

    def oberste_karte_abheben(self):
        """ Entfernt die oberste Karte vom Stapel """
        return self._karten.pop()
    
    def zufallskarte_ziehen(self):
        """ Zieht eine zufällige Karte aus dem Stapel aus entfernt diese, falls der Kartenstapel nicht leer ist """
        if self.karten:
            return self.karten.pop(random.randint(0,len(self) - 1)) 
        else:
            return None
    
    def mischen(self):
        """ Funktion durchmischt den Kartenstapel zufällig """
        return random.shuffle(self.karten)
    
    
if __name__=='__main__':
    s = Kartenstapel()
    print(s)


