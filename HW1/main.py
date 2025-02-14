#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from library import Sensor
from math import sqrt

def calculate_mean(sensor_obj, n_samples):
    sum_samples = 0
    i=0
    while i<n_samples:
        sample = sensor_obj.read()
        sum_samples += sample
        i+=1 
    return sum_samples/n_samples

def calculate_std(sensor_obj, n_samples):
    """Returns the standard deviation of the data samples."""
    exponent = 2
    mean = calculate_mean(sensor_obj, n_samples)
    return sqrt(sum(pow(sensor_obj.read() - mean, exponent) for _ in range(n_samples)) / n_samples)

def calculate_min(sensor_obj, n_samples):
    """Returns the smallest value of the data."""
    minimum_sample = 10
    for _ in range(n_samples):
        minimum_sample = min(minimum_sample, sensor_obj.read())
    return minimum_sample

def calculate_max(sensor_obj, n_samples):
    """Returns the largest value of the data."""
    maximum_sample = -1
    for _ in range(n_samples):
        maximum_sample = max(maximum_sample, sensor_obj.read())
    return maximum_sample

def calculate_range(sensor_obj, n_samples):
    """Returns the difference between the largest and smallest data."""
    return calculate_max(sensor_obj, n_samples) - calculate_min(sensor_obj, n_samples)

def plot(sensor_obj, n_samples):
    """Prints a text-based chart of the sensor data, normalized to a maximum of 40 characters."""
    maximum_length = 40
    maximum_value = 5
    print('plot:')
    for _ in range(n_samples):
        print('X' * int(sensor_obj.read() / maximum_value * maximum_length))

def count_voltage(sensor_obj, n_samples):
    """Returns the counts of samples in three voltage categories: (below 0.25V, between 0.25V-0.75V, above 0.75V)"""
    below_025 = 0
    between_025_and_075 = 0
    above_075 = 0

    threshold_025 = 0.25
    threshold_075 = 0.75

    for _ in range(n_samples):
        sample = sensor_obj.read()
        if sample < threshold_025:
            below_025 += 1
        elif threshold_025 <= sample <= threshold_075:
            between_025_and_075 += 1
        else:
            above_075 += 1

    return below_025, between_025_and_075, above_075

def count(sensor_obj, n_samples):
    """Prints a text-based visualization of sample counts in three voltage categories."""
    below_025, between_025_and_075, above_075 = count_voltage(sensor_obj, n_samples)
    max_count = max(below_025, between_025_and_075, above_075, 1)
    maximum_length = 40

    print('count:')
    print('Below 0.25V : ' + 'X' * int((below_025 / max_count) * maximum_length))
    print('0.25V-0.75V : ' + 'X' * int((between_025_and_075 / max_count) * maximum_length))
    print('Above 0.75V : ' + 'X' * int((above_075 / max_count) * maximum_length))

def main():
    num_samples = 100
    sensor_obj = Sensor()       # sensor_obj.read() gives us a float value

    # call the first function and print the returned value
    print("mean:", calculate_mean(sensor_obj, num_samples))
    
    # call here the additional functions
    print('std:', calculate_std(sensor_obj, num_samples))

    print('minimum:', calculate_min(sensor_obj, num_samples))

    print('maximum:', calculate_max(sensor_obj, num_samples))

    plot(sensor_obj, num_samples)

    count(sensor_obj, num_samples)

if __name__ == '__main__':
    main()
    