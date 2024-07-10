import numpy as np
import pandas as pd

def task1_category_vendor_sales(df : pd.DataFrame):
    '''
    Die Funktion bekommt einen DataFrame in der Struktur wie "Iowa_Liquor_Sales2020-21" Dataset übergeben.
    Gibt einen DataFrame zurück, in dem je Kategorie (Feld Category Name) und Hersteller (Feld 
    Vendor Name) der Gesamtumsatz (Feld Sale (Dollars)) berechnet wird (absteigend sortiert nach "Sale").
    '''
    return df.groupby(['Category Name', 'Vendor Name']).agg({'Sale (Dollars)': np.sum}).sort_values('Sale (Dollars)', ascending=False)


def task1_category_item_ranking_top3(df : pd.DataFrame):
    '''
    Die Funktion bekommt einen DataFrame in der Struktur wie "Iowa_Liquor_Sales2020-21" Dataset übergeben.
    Gibt einen DataFrame zurück, in dem nur die Top 3 Artikel pro Kategorie enthalten sind.
    sortiert absteigend nach Sale (Dollars).
    '''
    cols = ['Category Name', 'Item Description', 'Sale (Dollars)']
    small_df = df[cols].copy()
    subs = small_df.groupby(['Category Name', 'Item Description'], as_index=False).sum()
    subs['rankings_in_category'] = subs.groupby('Category Name', as_index=False).rank(ascending=False)
    subs = subs[subs['rankings_in_category'] <= 3]
    return subs.sort_values('Sale (Dollars)', ascending=False)


if __name__=='__main__':
    df = pd.read_parquet("Iowa_Liquor_Sales2020-21.parquet")
    # Aufruf mit gesamtem DataFrame
    print(task1_category_vendor_sales(df))
    # Aufruf mit einem Ausschnitt der Daten
    print(task1_category_vendor_sales(df.sample(int(0.5*len(df)), random_state=0)))
    
    # Aufruf mit gesamtem DataFrame
    print(task1_category_item_ranking_top3(df))
    # weitere Funktionstests sind hier möglich ...
    