import random


class Spielkarte():
    """ Klasse zur Repräsentation einer Spielkarte (v2) """

    def __init__(self, farbe=None, wert=None):
        """ Konstruktor für eine Karte mit übergebenen Argumenten
            für farbe und wert. Wird keine Farbe oder/und Wert übergeben,
            dann werden sie zufällig gesetzt."""
        
        # CODE FÜR AUFGABE 1 HIER EINFÜGEN
        if not (farbe and wert):
            farbe = random.choice(Kartenspiel.standardfarben)
            wert = random.choice(Kartenspiel.standardwerte)
        elif not farbe:
            farbe = random.choice(Kartenspiel.standardfarben)
        elif not wert:
            wert = random.choice(Kartenspiel.standardwerte)

        self._farbe = farbe  # Markieren als privates Attribut
        self._wert = wert # Markieren als privates Attribut

    def __eq__(self, other):
        """ logische Prüfung auf Gleichheit von zwei Spielkarten """
        return self.farbe == other.farbe and self.wert == other.wert

   
    @property
    def farbe(self):
        """ get-Methode von Attribut farbe """
        return self._farbe

    @farbe.setter
    def farbe(self, value):
        self._farbe = value


    @property
    def wert(self):
        """ get-Methode von Attribut wert """
        return self._wert

    @wert.setter
    def wert(self, value):
        self._wert = value

    def __str__(self):
        return f"{self.farbe} {self.wert}"




class Kartenspiel():
    """ Klasse, die ein Kartenspiel repräsentiert """

    standardfarben = ['kreuz', 'pik', 'karo', 'herz']  # statische Variable farben --> Zugriff über Kartenspiel.farben (auch außerhalb der Klasse)
    standardwerte = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'bube', 'dame', 'koenig', 'as'] # statische Variable farben --> Zugriff über Kartenspiel.werte (auch außerhalb der Klasse)
    

    def __init__(self, farben=None, werte=None):
        """ Konstruktor: legt ein Kartenspiel mit allen Kombinationen der übergebenen Farben und Werte an. 
            Wurden keine Farben übergeben, dann werden Standardfarben verwendet ('kreuz', 'pik', 'karo', 'herz').
            Wurden keine Werte übergeben, dann werden Standardwerte verwendet (2, 3, 4, 5, 6, 7, 8, 9, 10, 'bube', 'dame', 'koenig', 'as').
        """
        
        # Prüft, ob eines der Attribute nicht übergeben wurde und setzt ggf.  Standardwerte
        if not farben:
            farben = Kartenspiel.standardfarben
        if not werte:
            werte = Kartenspiel.standardwerte
        

        self._spielkarten = []  # Liste mit allen Spielkarten im Spiel

        # alle Kombinationen aus Farben und Werten anlegen
        for f in farben:
            for w in werte:
                self._spielkarten.append(Spielkarte(farbe=f, wert=w))
        

    def __str__(self):
        """ Gibt das  Kartenspiel als String aus """
        return f"Kartenspiel mit {len(self)} Karten (erste Karte: {self._spielkarten[0]}, letzte Karte: {self._spielkarten[-1]})"

    def __len__(self):
        """ Gibt die Anzahl der Karten im Kartenspiel zurück bei Aufruf von len() """
        return len(self._spielkarten)

    def __iter__(self):
        """ Initialisiert einen Iterator """
        self._i = 0  # Initalisierung des Iterators (Startindex 0)
        return self
    
    def __next__(self):
        """ Liefert die nächste Karte bis zum Ende der in einer Liste gespeicherten Spielkarten """ 
        if self._i < len(self._spielkarten):
            karte = self._spielkarten[self._i]
            self._i += 1
            return karte
        else:
            raise StopIteration()

class Doppelkopf(Kartenspiel):
    """ Klasse, repräsentiert das Kartenspiel "Doppelkopf" und erbt alle Funktionen der Klasse "Kartenspiel" """

    def __init__(self):
        """ Konstruktor: legt das Kartenspiel "Doppelkopf" an mit doppelter Anzahl an Spielkarten
                          (alle möglichen Kombinationen der Farben und Werte kommen doppelt vor). """
        super().__init__()
        self._spielkarten = self. _spielkarten * 2

class Skat(Kartenspiel):
    """ Klasse, repräsentiert das Kartenspiel "Skat" und erbt alle Funktionen der Klasse "Kartenspiel" """

    def __init__(self):
        """ Konstruktor: legt legt das Kartenspiel "Doppelkopf" an ohne die Wert 2,3,4,5 und 6. """
        super().__init__(werte=Kartenspiel.standardwerte[5:])

if __name__=='__main__':
    print(Spielkarte())
    print(Kartenspiel())
    print(Doppelkopf())  # kann einkommentiert werden nach Lösung von Aufgabe 3
    print(Skat())  # kann einkommentiert werden nach Lösung von Aufgabe 3
    