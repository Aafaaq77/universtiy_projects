def write_to_gbq(request):

    # importing all the necessary packages
    # must be included in requirements.txt
    from google.cloud import bigquery
    import gcsfs
    import pandas as pd
    import datetime
    import holidays
    from meteostat import Hourly
    # path to gcs, where the files are located
    file_path = 'gs://dscb430-analysis-data-bucket/raw_data/ETL_Data.csv'
    stations_file = 'gs://dscb430-analysis-data-bucket/raw_data/Capital_Bike_Share_Locations.csv'

    project_id = 'welu420'

    try:
        # accessing new rides
        new_rides = pd.read_csv(file_path, parse_dates=['Start_date', 'End_date'])

        # getting stations info
        station_infos = pd.read_csv(stations_file)
    except Exception as e:
        print('Unable to read in file', e, sep='\n')
        exit(1)

    # Transformations
    ###########################################################################
    # selecting specific columns
    # we need coordinates and capacity of a station
    cols = ['LATITUDE', 'LONGITUDE', 'NAME', 'CAPACITY']
    station_infos = station_infos[cols]
    station_infos = station_infos[cols]
    # getting station infos of the start station
    new_rides = pd.merge(new_rides, station_infos, left_on='Start_station', right_on='NAME')
    new_rides.rename(columns={
        'LATITUDE': 'start_lat',
        'LONGITUDE': 'start_lon',
        'CAPACITY': 'Start_capacity'
    }, inplace=True)
    # removing the extra column generated by merge
    new_rides.drop('NAME', axis=1, inplace=True)
    # getting station infos of the end station
    new_rides = pd.merge(new_rides, station_infos, left_on='End_station', right_on='NAME')
    new_rides.rename(columns={
        'LATITUDE': 'end_lat',
        'LONGITUDE': 'end_lon',
        'CAPACITY': 'End_capacity'
    }, inplace=True)
    # removing the extra column generated by merge
    new_rides.drop('NAME', axis=1, inplace=True)
    cols_order = ['Bike_number', 'Duration', 'Start_date', 'End_date', 'Start_station', 'Start_station_number',
              'Start_capacity', 'End_station', 'End_station_number', 'End_capacity', 'start_lat', 'start_lon',
              'end_lat', 'end_lon', 'Member_type', 'Holiday', 'temp', 'rel_humidity', 'precipitation', 'snow',
              'wspd', 'sun_minutes']

    # get holiday
    # if it was a holiday on that day
    rides_holiday = holidays.country_holidays('US', subdiv='DC', years=list(new_rides.Start_date.dt.year.unique()))
    new_rides['Holiday'] = new_rides.Start_date.dt.normalize().map(rides_holiday)
    year, month = new_rides.Start_date.dt.year.iloc[0], new_rides.Start_date.dt.month.iloc[0]
    day, hour = new_rides.Start_date.dt.day.iloc[0], new_rides.Start_date.dt.hour.iloc[0]

    # get weather
    # getting all the weather info which could be used for different purposes
    start_date = datetime.datetime(year, month, day, hour)
    year, month = new_rides.End_date.dt.year.iloc[0], new_rides.End_date.dt.month.iloc[0]
    day, hour = new_rides.End_date.dt.day.iloc[0], new_rides.End_date.dt.hour.iloc[0]
    end_date = datetime.datetime(year, month, day, hour)
    weather_station_id = '72405'  # weather station near DC
    weather_data = Hourly(weather_station_id, start=start_date, end=end_date).fetch()
    weather_cols = {
        'dwpt': 'dew_point', 'rhum': 'rel_humidity', 'prcp': 'precipitation',
        'tsun': 'sun_minutes'
    }
    weather_data.rename(columns=weather_cols, inplace=True)
    weather_data = weather_data.drop(['pres', 'coco'], axis=1)
    weather_data.reset_index(inplace=True)
    new_rides = new_rides.merge(weather_data,
                    left_on=[new_rides.Start_date.dt.normalize(),new_rides.Start_date.dt.hour],
                    right_on=[weather_data.time.dt.normalize(),weather_data.time.dt.hour])

    # removing extra columns
    new_rides.drop(columns=['key_0','key_1','time','dew_point','wdir','wpgt'], inplace=True)
    new_rides.set_index('ride_id', inplace=True)
    new_rides = new_rides[cols_order]  # match the schema of our BigQuery table
    ###########################################################################
    # End of transformations
    
    # write the new and transformed rides back to BigQuery table
    new_rides.to_gbq(
    'Bikesharing.System_Data',
    project_id,
    if_exists='append',
    )
    ###########################################################################
    # End of pipeline

    return 'ETL Pipeline completed successfully'

