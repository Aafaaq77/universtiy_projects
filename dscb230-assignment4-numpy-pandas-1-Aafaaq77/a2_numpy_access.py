import numpy as np

# mit diesem Arrays werden wir arbeiten
arr1 = np.array([[1., 2., 1., 1., 8.],[3., 6., 7., 2., 5.],[2., 8., 5., 8., 1.],[6., 3., 8., 9., 1.],[1., 6., 4., 5., 3.],[2., 6., 3., 6., 8.],[9., 8., 4., 4., 5.],[4., 5., 7., 6., 7.],[5., 9., 1., 9., 1.],[9., 9., 5., 1., 1.],[5., 3., 1., 4., 3.],[1., 5., 6., 9., 6.],[5., 3., 9., 2., 8.],[2., 7., 9., 7., 7.],[1., 4., 7., 3., 1.],[5., 6., 7., 3., 4.],[3., 8., 8., 7., 6.],[1., 9., 2., 2., 7.],[1., 3., 4., 5., 8.],[6., 9., 2., 9., 7.]])
arr2 = np.array([[5., 6., 5., 3., 5.],[4., 8., 2., 1., 2.],[7., 4., 5., 7., 3.],[1., 9., 5., 1., 4.],[2., 7., 8., 8., 4.],[4., 2., 8., 3., 6.],[8., 1., 9., 1., 2.],[6., 4., 3., 7., 3.],[8., 8., 2., 9., 5.],[4., 7., 3., 3., 3.],[1., 2., 8., 6., 7.],[2., 5., 4., 4., 4.],[3., 8., 9., 5., 4.],[8., 7., 9., 6., 6.],[8., 6., 5., 6., 4.],[9., 1., 7., 4., 6.],[6., 1., 6., 3., 9.],[1., 5., 1., 7., 6.],[6., 9., 1., 7., 5.],[9., 7., 8., 6., 4.]])

def task2_stepwise(arr):
    '''
    args:
        arr(np.array): ein Array
    returns:
        ein Array -> Zeile zwei bis drittletzte Zeile (nicht inklusiv) und alle Spalten bis
            zweitletzte Spalte (nicht inklusiv)
    '''
    return arr[2:-3:3, :-2]

def task2_masked_selection_sum(arr):
    '''
    args:
        arr(np.array): ein Array
    returns:
        Summe der Werte, die größer als Median des Array sind
    '''
    med = np.median(arr, axis=0)
    return np.sum(arr[arr > med])

if __name__=='__main__':
    print(task2_stepwise(arr2))
    
    # weitere Funktionstests sind hier möglich
    