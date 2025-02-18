#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from matplotlib import pyplot as plt
from os import path

MINIMUM_DATA = None
MAXIMUM_DATA = None

def validate_data(data):
    if not data: raise ValueError("The data list is empty.")  

def validate_min_max():
    if MINIMUM_DATA is None or MAXIMUM_DATA is None: raise ValueError("Global min and max are not set. Ensure stats() is called first.")

def read_data(file_name):
    """Returns a list of floats after reading the content of data.dat"""
    if not path.isfile(file_name): raise FileNotFoundError("The file was not found.")
    with open(file_name, "r") as raw_file: return [float(line.strip()) for line in raw_file if line.strip()]   

def calculate_average(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    return sorted_data[mid] if len(sorted_data) % 2 else (sorted_data[mid - 1] + sorted_data[mid]) / 2

def stats(data):
    """Returns the average, median, minimum, and maximum values of the list passed as argument."""
    global MINIMUM_DATA, MAXIMUM_DATA
    MINIMUM_DATA, MAXIMUM_DATA = min(data), max(data)
    return calculate_average(data), calculate_median(data), MINIMUM_DATA, MAXIMUM_DATA

def normalize(data):
    """Returns the normalized list of all values between 0 and 1 based on the minimum and maximum values."""
    if MINIMUM_DATA == MAXIMUM_DATA: return [0] * len(data)
    return [(x - MINIMUM_DATA) / (MAXIMUM_DATA - MINIMUM_DATA) for x in data]

def moving_average(data, window_size):
    """Returns a new list where each element is the average of the previous window_size elements."""
    if window_size <= 0: raise ValueError("Window size must be greater than zero.")
    return [sum(data[i:i+window_size]) / len(data[i:i+window_size]) for i in range(len(data) - window_size + 1)]

def count(data, bins):
    """Returns the count of data samples per bin."""
    if bins <= 0: raise ValueError("Bin size must be greater than zero")
    bin_width = (MAXIMUM_DATA - MINIMUM_DATA) / bins
    return [sum(MINIMUM_DATA + i * bin_width <= x < MINIMUM_DATA + (i + 1) * bin_width for x in data) for i in range(bins - 1)] + [sum(x >= MINIMUM_DATA + (bins - 1) * bin_width for x in data)]

def plot(data, start, end, average, minimum, maximum):
    """Creates a chart that shows the average, min, and max values obtained by stats."""
    if start < 0 or end > len(data) or start >= end: raise ValueError("Invalid start or end indices.")

    data_slice = data[start:end]

    plt.figure(figsize=(10,6))
    plt.plot(data_slice, marker='o', linestyle='-', color='b', label='Data')

    plt.axhline(y=average, color='r', linestyle='--', label=f"Average: {average:.2f}")
    plt.axhline(y=minimum, color='g', linestyle='--', label=f"Min: {minimum:.2f}")
    plt.axhline(y=maximum, color='purple', linestyle='--', label=f"Max: {maximum:.2f}")

    plt.title("Data Visualization with Statistics")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()

    plt.savefig("chart1.png")
    print("Plot saved as chart1.png")

def plot_count(bin_count):
    """Creates a bar chart that shows the output of bin count in ascending order."""
    if not bin_count or any(b < 0 for b in bin_count): raise ValueError("Invalid bin count result.")

    sorted_bins = sorted(bin_count)

    plt.figure(figsize=(8, 6))
    plt.bar(range(len(sorted_bins)), sorted_bins, color='b')

    plt.title("Bin Count Results (Ascending Order)")
    plt.ylabel("Frequency")

    plt.savefig("chart2.png")
    print("Plot saved as chart2.png")

def main():
    data = read_data("data.dat")

    validate_data(data)

    average, median, minimum, maximum = stats(data)

    validate_min_max()

    normal = normalize(data)

    moving_avg = moving_average(data, 1)

    bin_count = count(data, 4)

    plot(data, 0, 50, average, minimum, maximum)

    plot_count(bin_count)

    plt.close()

if __name__ == '__main__':
    main()
