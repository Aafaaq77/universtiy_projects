import numpy as np
import pandas as pd

def task2_sales_per_capita(df : pd.DataFrame):
    '''
    Die Funktion bekommt einen DataFrame in der Struktur wie "Iowa_Liquor_Sales2020-21" Dataset übergeben.
    Gibt einen DataFrame zurück, in dem für jede Stadt der Umsatz (Feld Sale (Dollars)) sowie Absatz in 
    Liter (Feld Volume Sold (Liters)) pro Einwohner errechnet wird -> „turnover_per_capita“ und
     „sold_liters_per_capita“ heißen die neuen Spalten.
    Der DataFrame ist absteigend nach turnover_per_capita sortiert und es werden nur die 
    obersten 10 Zeilen zurückgegeben.
    Für die Spalte "Population" wird die Datei "poplation.csv" benutzt.
    '''
    iowa_population = pd.read_csv('population.csv')
    cols = ['City', 'Sale (Dollars)', 'Volume Sold (Liters)']
    small_df = df[cols].copy()
    city_merge = pd.merge(small_df, iowa_population, left_on='City', right_on='City')
    aggregated = city_merge.groupby('City',
                   as_index=False).agg({'Sale (Dollars)': np.sum,
                                        'Volume Sold (Liters)': np.sum,
                                        'Population': np.mean})
    aggregated['turnover_per_capita'] = aggregated['Sale (Dollars)']/aggregated['Population']
    aggregated['sold_liters_per_capita'] = aggregated['Volume Sold (Liters)']/aggregated['Population']

    return aggregated.sort_values('turnover_per_capita', ascending=False).head(10)


if __name__=='__main__':
    df = pd.read_parquet("Iowa_Liquor_Sales2020-21.parquet")
    # Aufruf mit gesamtem DataFrame
    print(task2_sales_per_capita(df))
    
    # weitere Funktionstests sind hier möglich ...
    