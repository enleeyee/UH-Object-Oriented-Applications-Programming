#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from csv import DictReader
from math import inf
from os import path

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
WEATHER_YEARS = ('2006', '2010', '2011', '2012', '2013', '2014', '2015', '2018', '2019', '2021')
YEAR_LENGTH = 10

def to_float(value, default = 0.0):
    """Converts valid values into floats or default value 0.0."""
    try:
        return float(value)
    except ValueError:
        return default

def mean(values):
    """Returns the mean of values or 0 if not valid."""
    return sum(values) / len(values) if values else 0

def ratio(count, total):
    """Returns the ratio of values or 0 if not valid."""
    return count / total if total else 0

def is_hot(temp_avg):
    """Returns True if the temperature is hot."""
    return temp_avg >= 85

def is_rainy(rainfall):
    """Returns True if there has been rain."""
    return rainfall > 0

def is_fair_or_partly_cloudy(cloud9am, cloud3pm):
    """Returns True if there are fair or partly cloudy."""
    return cloud9am in {'Fair', 'Partly Cloudy'} or cloud3pm in {'Fair', 'Partly Cloudy'}

def is_warm_season(month):
    """Returns True if the month is in the warm season (March–October)."""
    return 3 <= month <= 10

def split_by_season(rows):
    """Splits weather data into warm and cold season lists."""
    warm_season, cold_season = [], []
    for row in rows:
        month = int(row['date'].split('-')[1])
        (warm_season if is_warm_season(month) else cold_season).append(row)
    return warm_season, cold_season

def read_weather_data(file_name):
    """Reads weather data from a CSV file and returns a summary dictionary."""
    with open(file_name, newline='') as csv_file:
        reader = DictReader(csv_file)
        rows = list(reader)
    return read_weather_data_from_rows(rows)

def read_weather_data_2(file_name):
    """Reads weather data and returns summaries for warm and cold seasons."""
    with open(file_name, newline='') as csv_file:
        reader = DictReader(csv_file)
        warm_rows, cold_rows = split_by_season(list(reader))
    return {
        'warm': read_weather_data_from_rows(warm_rows),
        'cold': read_weather_data_from_rows(cold_rows),
    }

def read_weather_data_from_rows(rows):
    """Processes a list of rows into a summary dictionary."""
    temperatures, rainfalls, wind_speeds, humidities, pressures = [], [], [], [], []
    min_temp, max_temp = inf, -inf
    hot_days, rainy_days, fair_days, total_days = 0.0, 0.0, 0.0, 0.0

    for row in rows:
        temp_avg = (to_float(row['temp9am']) + to_float(row['temp3pm'])) / 2
        wind_avg = (to_float(row['wind_speed9am']) + to_float(row['wind_speed3pm'])) / 2
        humidity_avg = (to_float(row['humidity9am']) + to_float(row['humidity3pm'])) / 2
        pressure_avg = (to_float(row['pressure9am']) + to_float(row['pressure3pm'])) / 2

        temperatures.append(temp_avg)
        min_temp = min(min_temp, to_float(row['min_temp']))
        max_temp = max(max_temp, to_float(row['max_temp']))
        rainfalls.append(to_float(row['rainfall']))
        wind_speeds.append(wind_avg)
        humidities.append(humidity_avg)
        pressures.append(pressure_avg)

        hot_days += is_hot(temp_avg)
        rainy_days += is_rainy(to_float(row['rainfall']))
        fair_days += is_fair_or_partly_cloudy(row['cloud9am'], row['cloud3pm'])
        total_days += 1

    return {
        'a_temp': mean(temperatures),
        'a_min_temp': 0.0 if min_temp == inf else min_temp,
        'a_max_temp': 0.0 if max_temp == -inf else max_temp,
        'a_rainfall': mean(rainfalls),
        'a_wind': mean(wind_speeds),
        'a_humidity': mean(humidities),
        'a_pressure': mean(pressures),
        'p_hot': ratio(hot_days, total_days),
        'p_rain': ratio(rainy_days, total_days),
        'p_sunshine': ratio(fair_days, total_days),
    }

def _process_humidity_generic(summary_data, extractor):
    """Generic function to process humidity data using the given extractor function."""
    return {WEATHER_YEARS[i]: extractor(summary_data[i]) for i in range(YEAR_LENGTH)} if summary_data else []

def process_humidity(summary_years):
    """Returns a dictionary of average humidity values per year."""
    return _process_humidity_generic(summary_years, lambda summary: summary['a_humidity'])

def process_humidity_2(summary_season_years):
    """Returns a dictionary of average humidity values per year for warm and cold seasons."""
    return {
        'warm': _process_humidity_generic(summary_season_years, lambda summary: summary['warm']['a_humidity']),
        'cold': _process_humidity_generic(summary_season_years, lambda summary: summary['cold']['a_humidity']),
    }

def _create_summary_year_generic(summary_data, extractor):
    """Generic function to extract a list of attributes from summary data using an extractor function."""
    return [extractor(year) for year in summary_data] if summary_data else []

def process_sunshine(summary_years):
    """Returns the smallest and the largest sunshine ratios for the observation period."""
    sunshine_ratios = _create_summary_year_generic(summary_years, lambda summary: summary['p_sunshine'])
    return min(sunshine_ratios), max(sunshine_ratios)

def process_sunshine_2(summary_season_years):
    """Returns the smallest and the largest sunshine ratios for the observation period for warm and cold seasons."""
    warm_sunshine_ratios = _create_summary_year_generic(summary_season_years, lambda summary: summary['warm']['p_sunshine'])
    cold_sunshine_ratios = _create_summary_year_generic(summary_season_years, lambda summary: summary['cold']['p_sunshine'])
    return {
        'warm': (min(warm_sunshine_ratios), max(warm_sunshine_ratios)),
        'cold': (min(cold_sunshine_ratios), max(cold_sunshine_ratios)),
    }

def process_temperature(summary_years):
    """Returns four lists: average temperatures, minimum temperatures, maximum temperatures, and hot day ratios per year."""
    return (
        _create_summary_year_generic(summary_years, lambda summary: summary['a_temp']),
        _create_summary_year_generic(summary_years, lambda summary: summary['a_min_temp']),
        _create_summary_year_generic(summary_years, lambda summary: summary['a_max_temp']),
        _create_summary_year_generic(summary_years, lambda summary: summary['p_hot']),
    )

def process_temperature_2(summary_season_years):
    """Returns four lists: average temperatures, minimum temperatures, maximum temperatures, and hot day ratios per year for warm and cold seasons."""
    return {
        'warm': (
            _create_summary_year_generic(summary_season_years, lambda summary: summary['warm']['a_temp']),
            _create_summary_year_generic(summary_season_years, lambda summary: summary['warm']['a_min_temp']),
            _create_summary_year_generic(summary_season_years, lambda summary: summary['warm']['a_max_temp']),
            _create_summary_year_generic(summary_season_years, lambda summary: summary['warm']['p_hot']),
        ),
        'cold': (
            _create_summary_year_generic(summary_season_years, lambda summary: summary['cold']['a_temp']),
            _create_summary_year_generic(summary_season_years, lambda summary: summary['cold']['a_min_temp']),
            _create_summary_year_generic(summary_season_years, lambda summary: summary['cold']['a_max_temp']),
            _create_summary_year_generic(summary_season_years, lambda summary: summary['cold']['p_hot']),
        ),
    }

def main():
    weather_summary_years = []
    for year in WEATHER_YEARS:
        csv_file_path = path.join(BASE_DIR, 'archive', f'htx_{year}_weather.csv')
        weather_summary_years.append(read_weather_data(csv_file_path))

    print('Humidity:', process_humidity(weather_summary_years))
    print('Sunshine:', process_sunshine(weather_summary_years))
    print('Temperature:', process_temperature(weather_summary_years))

    weather_season_summary_years = []
    for year in WEATHER_YEARS:
        csv_file_path = path.join(BASE_DIR, 'archive', f'htx_{year}_weather.csv')
        weather_season_summary_years.append(read_weather_data_2(csv_file_path))

    print('Humidity:', process_humidity_2(weather_season_summary_years))
    print('Sunshine:', process_sunshine_2(weather_season_summary_years))
    print('Temperature:', process_temperature_2(weather_season_summary_years))

if __name__ == '__main__':
    main()
