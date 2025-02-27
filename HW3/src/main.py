#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from csv import DictReader
from math import inf

def mean(values):
    return sum(values) / len(values) if values else 0

def ratio(count, total):
    return count / total if total else 0

def is_hot(temp_avg):
    return temp_avg >= 85

def is_rainy(rainfall):
    return rainfall > 0

def is_fair_or_partly_cloudy(cloud9am, cloud3pm):
    return cloud9am in {"Fair", "Partly Cloudy"} or cloud3pm in {"Fair", "Partly Cloudy"}

def read_weather_data(file_name):
    """Reads weather data from a CSV file and returns a summary dictionary."""
    temperatures, rainfalls, wind_speeds, humidities, pressures = [], [], [], [], []
    min_temp, max_temp = inf, -inf
    hot_days, rainy_days, fair_days, total_days = 0, 0, 0, 0

    with open(file_name, newline='') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            temp_avg = (float(row['temp9am']) + float(row['temp3pm'])) / 2
            wind_avg = (float(row['wind_speed9am']) + float(row['wind_speed3pm'])) / 2
            humidity_avg = (float(row['humidity9am']) + float(row['humidity3pm'])) / 2
            pressure_avg = (float(row['pressure9am']) + float(row['pressure3pm'])) / 2

            temperatures.append(temp_avg)
            min_temp = min(min_temp, float(row['min_temp']))
            max_temp = max(max_temp, float(row['max_temp']))
            rainfalls.append(float(row['rainfall']))
            wind_speeds.append(wind_avg)
            humidities.append(humidity_avg)
            pressures.append(pressure_avg)

            hot_days += is_hot(temp_avg)
            rainy_days += is_rainy(float(row['rainfall']))
            fair_days += is_fair_or_partly_cloudy(row['cloud9am'], row['cloud3pm'])
            total_days += 1

    return {
        'a_temp': mean(temperatures),
        'a_min_temp': min_temp,
        'a_max_temp': max_temp,
        'a_rainfall': mean(rainfalls),
        'a_wind': mean(wind_speeds),
        'a_humidity': mean(humidities),
        'a_pressure': mean(pressures),
        'p_hot': ratio(hot_days, total_days),
        'p_rain': ratio(rainy_days, total_days),
        'p_sunshine': ratio(fair_days, total_days)
    }

def main():
    print(read_weather_data("./archive/test.csv"))

if __name__ == '__main__':
    main()
