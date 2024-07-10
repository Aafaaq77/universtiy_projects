from kartenspiel import Spielkarte, Kartenspiel
import random


def create_random_spielkarte():
    """
    Erzeugt eine Instanz der Klasse "Spielkarte" mit zufälliger Farbe und zufälligem Wert
    returns: Die erzeugte Instanz
    """
    farbe = random.choice(Kartenspiel.standardfarben)
    wert = random.choice(Kartenspiel.standardwerte)
    return Spielkarte(farbe, wert)


def create_doppelkopf():
    """ 
    Erzeugt eine Liste mit doppelter Anzahl an Objekten der Spielkarte "Klasse"
    (alle möglichen Kombinationen der Farben und Werte kommen doppelt vor)  
    """
    return [Spielkarte(farbe, wert) for farbe in Kartenspiel.standardfarben for wert in Kartenspiel.standardwerte]*2
    






