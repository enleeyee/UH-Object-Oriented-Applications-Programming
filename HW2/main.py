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

# read_data: Returns a list of floats after reading the content of data.dat. The name of the file is passed as the single argument of this function.
def read_data(file_name):
    if not path.isfile(file_name): raise FileNotFoundError("The file was not found.")
    with open(file_name, "r") as raw_file: return [float(line.strip()) for line in raw_file if line.strip()]   

# stats: Accepts a list of floats as input. It returns the average, median, minimum, and maximum values of the list passed as argument. Note that the median is the middle element of the sorted list. If the number of elements is even, then the median is the average of the two middle elements.
def calculate_average(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    mid = len(sorted_data) // 2
    return sorted_data[mid] if len(sorted_data) % 2 else (sorted_data[mid - 1] + sorted_data[mid]) / 2

def stats(data):
    global MINIMUM_DATA, MAXIMUM_DATA
    MINIMUM_DATA, MAXIMUM_DATA = min(data), max(data)
    return calculate_average(data), calculate_median(data), MINIMUM_DATA, MAXIMUM_DATA

# normalize: Accepts a list of floats and scales all values between 0 and 1 based on the minimum and maximum values. The function returns the normalized list. Implement the operation yourself.
def normalize(data):
    if MINIMUM_DATA == MAXIMUM_DATA: return [0] * len(data)
    return [(x - MINIMUM_DATA) / (MAXIMUM_DATA - MINIMUM_DATA) for x in data]

# moving_average: Accepts a list of floats and a window size. It returns a new list where each element is the average of the previous window_size elements. You may use sum.
def moving_average(data, window_size):
    if window_size <= 0: raise ValueError("Window size must be greater than zero.")
    return [sum(data[i:i+window_size]) / len(data[i:i+window_size]) for i in range(len(data) - window_size + 1)]

# count: Accepts a list of floats as input and one integer that indicates the number of bins. Your function splits the range of data values into that number of bins and returns the count of data samples per bin. You must implement this operation (do not use a library to do the job).
def count(data, bins):
    if bins <= 0: raise ValueError("Bin size must be greater than zero")
    bin_width = (MAXIMUM_DATA - MINIMUM_DATA) / bins
    return [sum(MINIMUM_DATA + i * bin_width <= x < MINIMUM_DATA + (i + 1) * bin_width for x in data) for i in range(bins - 1)] + [sum(x >= MINIMUM_DATA + (bins - 1) * bin_width for x in data)]

# plot: Create a Matplotlib chart of a slice of the data that lies within the range provided as input (i.e., start and end indices, excluding the end index). In addition to the data sample values, the chart shows the average, min, and max values obtained by stats as horizontal lines. Make sure that you label the axes and plots properly. Save the chart in PNG format to a file named: chart1.png.
def plot(data, start, end, average, minimum, maximum):
    if start < 0 or end > len(data) or start >= end: raise ValueError("Invalid start or end indices.")

    data_slice = data[start:end]

    plt.figure(figsize=(10,6))
    plt.plot(data_slice, marker='o', linestyle='-', color='b', label='Data')

    plt.axhline(y=average, color='r', linestyle='--', label=f"Average: {average:.2f}")
    plt.axhline(y=minimum, color='g', linestyle='--', label=f"Min: {minimum:.2f}")
    plt.axhline(y=maximum, color='purple', linestyle='--', label=f"Max: {maximum:.2f}")

    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Data Visualization with Statistics")
    plt.legend()

    plt.savefig("chart1.png")
    print("Plot saved as chart1.png")

    plt.show()

# plot_count: Create a Matplotlib chart of the bin count results in ascending order, i.e, of the output of count. No need to label the horizontal axis in this case. Use bar not hist. Save the chart in PNG format to a file named: chart2.png.


def main():
    data = read_data("data.dat")

    validate_data(data)

    average, median, minimum, maximum = stats(data)

    validate_min_max()

    print(normalize(data))

    print(moving_average(data, 1))

    print(count(data, 4))

    plot(data, 0, 50, average, minimum, maximum)

if __name__ == '__main__':
    main()
