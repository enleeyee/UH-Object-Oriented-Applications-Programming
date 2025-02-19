#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from matplotlib import pyplot as plt
from os import path

def validate_data(data_samples):
    if not data_samples: raise ValueError("The data list is empty.")  

def read_data(file_name):
    """Returns a list of floats after reading the content of data.dat"""
    if not path.isfile(file_name): raise FileNotFoundError("The file was not found.")
    with open(file_name, "r") as data_file: return [float(line.strip()) for line in data_file if line.strip()]   

def calculate_average(data_samples):
    return sum(data_samples) / len(data_samples)

def calculate_median(data_samples):
    sorted_data = sorted(data_samples)
    mid = len(sorted_data) // 2
    return sorted_data[mid] if len(sorted_data) % 2 else (sorted_data[mid - 1] + sorted_data[mid]) / 2

def stats(data_samples):
    """Returns the average, median, minimum, and maximum values of the list passed as argument."""
    return calculate_average(data_samples), calculate_median(data_samples), min(data_samples), max(data_samples)

def normalize(data_samples, minimum, maximum):
    """Returns the normalized list of all values between 0 and 1 based on the minimum and maximum values."""
    if minimum == maximum: return [0] * len(data_samples)
    return [(x - minimum) / (maximum - minimum) for x in data_samples]

def moving_average(data_samples, window_size):
    """Returns a new list where each element is the average of the previous window_size elements."""
    if window_size <= 0 or window_size > len(data_samples): raise ValueError("Window size must be between 1 and the data length.")
    return [sum(data_samples[i:i+window_size]) / len(data_samples[i:i+window_size]) for i in range(len(data_samples) - window_size + 1)]

def count(data_samples, bins, minimum, maximum):
    """Returns the count of data samples per bin."""
    if bins <= 0: raise ValueError("Bin size must be greater than zero")
    bin_width = (maximum - minimum) / bins
    return [sum(minimum + i * bin_width <= x < minimum + (i + 1) * bin_width for x in data_samples) for i in range(bins - 1)] + [sum(x >= minimum + (bins - 1) * bin_width for x in data_samples)]

def plot(data_samples, start, end, average, minimum, maximum):
    """Creates a chart that shows the average, min, and max values obtained by stats."""
    if start < 0 or end > len(data_samples) or start >= end: raise ValueError("Invalid start or end indices.")

    data_slice = data_samples[start:end]

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
    data_samples = read_data("data.dat")
    validate_data(data_samples) # validate right after reading data.dat

    average, median, minimum, maximum = stats(data_samples)

    normalized_data = normalize(data_samples, minimum, maximum)
    moving_average_result = moving_average(data_samples, 1)

    bin_frequencies = count(data_samples, 4, minimum, maximum)

    plot(data_samples, 0, 50, average, minimum, maximum)
    plot_count(bin_frequencies)

    plt.close()

if __name__ == '__main__':
    main()
