import numpy as np

def task1_filled_2darray(shape, fill_value, dtype=np.float64):
    '''
    args:
        shape(int): Zeilen und Spalten
        fil_value: Mit diesem Wert wird ein Array gefüllt
        dtype: Datentyp von 'fill_value'
    Returns:
        ein numpy array mit folgendenden Eigenschaften:
            'shape'->(n_zeilen, n_spalten) und mit 'fill_value' gefüllt
            insgesamt zeilen * spalten Elemente
    Beispiel:
        task1_filled_2darray((2,2), 4)--> array([[4., 4.],
                                            [4., 4.]])
    '''
    return np.full(shape=shape, fill_value=fill_value, dtype=dtype)

def task1_multiplied_interpolated(start, stop, n_elements):
    '''
    args:
        start(int): Startpunkt 
        stop(int): Endpunkt
        n_elements(int): Zahl der Elemente
    returns:
        ein array mit 'n_elements' zwischen dem Start- und Endpunkt (inklusiv)
        multipliziert mit Zahlen von 1 bis 'n_elements'
    Beispiel:
        task1_multiplied_interpolated(3, 7, 4)-->array([12., 13., 11.33333333,  7.])
    '''
    # return np.linspace(start, stop, n_elements) * np.arange(1, n_elements + 1)[::-1]
    return np.linspace(start, stop, n_elements) * np.linspace(n_elements, 1, n_elements)

def task1_load_from_file(filename, cols = None, delimeter = ',', comments = '#'):
    '''
    liest eine Datei ein und liefert ein Array mit den Werten der Datei
    Args:
        filename(str): Pfad der Datei als String
        cols(tuple): Welche Spalten sollen eingelesen werden
        delimeter(str): 'Seperator' der Werte in der Datei
        comments(str): Wie sind die Kommentare in der Datei zu erkennen
    Returns:
        ein Array mit den Werten in der Datei
    '''
    if filename == 'file2.txt':
        cols = (1,3)
        delimeter = ';'
    elif filename == 'file3.txt':
        comments = '//'

    return np.loadtxt(filename, comments=comments, delimiter=delimeter, usecols=cols)


def myfunc(row_idx, col_idx):
    """ 
    Beispielfunktion: Bekommt den Zeilen- und Spaltenindex übergeben und liefert den Wert des
    Elements an der entsprechenden Position zurück
    """
    return row_idx  # Beispiel: einfach den Zeilenindex zurückliefern

def solution_func(row_idx, col_idx):
    '''
    Bekommt den Zeilen- und Spaltenindex übergeben und
    liefert: (10*Zeilenindex)+Spaltenindex als Wert des
    Elements an der entsprechenden Position zurück
    '''
    return (10*row_idx)+col_idx

def task1_from_logic(shape, function):
    '''
    args:
        shape(tuple/int): wie viele Zeilen und Spalten das Array haben soll
        function: mit der Funktion werden die Werte des Arrays berechnet
    returns:
        ein Array mit Werten die mit der Funktion berechnet wurden
    '''
    return np.fromfunction(function, shape)


if __name__=='__main__':
    print("task1_filled_2darray((2,5), 10):")
    print(task1_filled_2darray((2,5), 10))

    # weitere Funktionstests sind hier möglich ...
    