#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from csv import DictReader
from math import inf

def average(weighted_sum, size):
    return weighted_sum / size

def read_file(fileName):
    summary_dictionary = dict()
    average_temperature_sum = 0
    minimum_temperature = inf
    maximum_temperature = -inf
    average_rainfall_sum = 0
    average_windspeed_sum = 0
    average_humidity_sum = 0
    average_pressure_sum = 0
    length = 0

    with open(fileName, newline='') as csvFile:
        reader = DictReader(csvFile)
        for row in reader:
            average_temperature_sum += average((float(row['temp9am']) + float(row['temp3pm'])), 2)
            minimum_temperature = min(minimum_temperature, float(row['min_temp']))
            maximum_temperature = max(maximum_temperature, float(row['max_temp']))
            average_rainfall_sum += float(row['rainfall'])
            average_windspeed_sum += average((float(row['wind_speed9am']) + float(row['wind_speed3pm'])), 2)
            average_humidity_sum += average((float(row['humidity9am']) + float(row['humidity3pm'])), 2)
            average_pressure_sum += average((float(row['pressure9am']) + float(row['pressure3pm'])), 2)



            length += 1

    summary_dictionary['a_temp'] = average(average_temperature_sum, length)
    summary_dictionary['a_min_temp'] = minimum_temperature
    summary_dictionary['a_max_temp'] = maximum_temperature
    summary_dictionary['a_rainfall'] = average(average_rainfall_sum, length)
    summary_dictionary['a_wind'] = average(average_windspeed_sum, length)
    summary_dictionary['a_humidity'] = average(average_humidity_sum, length)
    summary_dictionary['a_pressure'] = average(average_pressure_sum, length)
    # summary_dictionary['p_hot'] = 
    # summary_dictionary['p_rain'] = 
    # summary_dictionary['p_sunshine'] = 

    return summary_dictionary

    # p_hot: the ratio of number of days with a temperature of 85 or more to the total number of days in that year
    # p_rain: the rainy day ratio (number of rainy days over total days in that year)
    # p_sunshine: the “fair” and “Partly Cloudy” to total number of days in that year
    # Note:
    # Please be aware that the data for temperature, wind speed, humidity, and pressure in the files are divided into two values per day: one recorded at 9 AM and another at 3 PM.
    # To simplify, consider the average value of the two, resulting in a single observation per day.
    # For cloud data, consider both observations, i.e., a day is considered cloudy if cloudy at 9 AM **or* cloudy at 3 PM.


def main():
    print(read_file("./archive/test.csv"))

if __name__ == '__main__':
    main()
