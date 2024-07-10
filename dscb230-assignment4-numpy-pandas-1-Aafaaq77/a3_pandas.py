import pandas as pd
import seaborn as sns  # importieren Sie dieses package auch in Jupyter, falls Sie dort auch arbeiten möchten

def task3_pandas():
    '''
    Liest ein default dataFrame der seaborn-Bibliothek ein
    returns:
        ein DataFrame mit Zeilen wo:
            1. Die Spalte 'mpg' größer als 95% aller Werte ist
            2. Die 'origin'-Spalte nicht gleich 'europe' ist oder 
               das Baujahr 'model_year' nicht von den 80ern ist.
    '''
    df = sns.load_dataset('mpg')
     
    percent = df['mpg'].quantile(0.95)
    # mask1 = df['mpg'] > percent
    # mask2 = df['origin'] != 'europe'
    
    # mask3 = ~df['model_year'].astype(str).str.startswith('8')
    # df_filtered = df[(mask1) & ((mask2) | (mask3))]
    skip_years = list(range(80,90))
    # return df_filtered  # DataFrame am Ende zurückgeben
    return df.query('(mpg > @percent) & ((origin != "europe") | (model_year not in @skip_years))')


if __name__=='__main__':
    print(task3_pandas())
    
    # weitere Funktionstests sind hier möglich
    