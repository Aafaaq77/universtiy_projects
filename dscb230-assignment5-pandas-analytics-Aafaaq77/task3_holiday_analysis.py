import numpy as np
import pandas as pd
import holidays

def task3_holiday_analysis(df : pd.DataFrame):
    '''
    Die Funktion bekommt einen DataFrame in der Struktur wie "Iowa_Liquor_Sales2020-21" Dataset übergeben.
    Gibt einen DataFrame zurück, in dem für jeden Feiertag von Iowa den mittleren Umsatz pro Feiertag
    berchnet wird. Es wird auch gezählt, wie oft dieser Tag Feiertag im übergebenen DataFrame vorkommt.
    Der DataFrame wird absteigend nach "Sale (Dollars)" sortiert.
    '''
    holidays_df = pd.DataFrame.from_dict(holidays.US(
        state='IA', years=list(range(df['Date'].min().year, df['Date'].max().year + 1))),
                        orient='index', columns=['Holiday'])
    holidays_df.index = pd.to_datetime(holidays_df.index)
    holidays_df.index.rename('Date', inplace=True)
    per_day = df.groupby( 'Date').agg({'Sale (Dollars)': 'sum'})
    merged_holidays = pd.merge(per_day, holidays_df, on='Date', how='left')
    merged_holidays['Holiday'].fillna('No Holiday', inplace=True)
    merged_holidays.rename(columns={'Holiday': 'HolidayName'}, inplace=True)

    return merged_holidays.groupby('HolidayName', as_index=False).agg(
        {'Sale (Dollars)': [np.mean, 'count']}).sort_values(('Sale (Dollars)', 'mean'), ascending=False)



if __name__=='__main__':
    df = pd.read_parquet("Iowa_Liquor_Sales2020-21.parquet")
    # Aufruf mit gesamtem DataFrame
    print(task3_holiday_analysis(df))
    
    # weitere Funktionstests sind hier möglich ...
    