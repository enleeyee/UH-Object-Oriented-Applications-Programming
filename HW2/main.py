#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ENLAI YII <edyii@cougarnet.uh.edu> (2064210)

from os import path

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
    if not data: raise ValueError("The data list is empty.")
    return calculate_average(data), calculate_median(data), min(data), max(data)

# normalize: Accepts a list of floats and scales all values between 0 and 1 based on the minimum and maximum values. The function returns the normalized list. Implement the operation yourself.

# moving_average: Accepts a list of floats and a window size. It returns a new list where each element is the average of the previous window_size elements. You may use sum.

# count: Accepts a list of floats as input and one integer that indicates the number of bins. Your function splits the range of data values into that number of bins and returns the count of data samples per bin. You must implement this operation (do not use a library to do the job).

# plot: Create a Matplotlib chart of a slice of the data that lies within the range provided as input (i.e., start and end indices, excluding the end index). In addition to the data sample values, the chart shows the average, min, and max values obtained by stats as horizontal lines. Make sure that you label the axes and plots properly. Save the chart in PNG format to a file named: chart1.png.

# plot_count: Create a Matplotlib chart of the bin count results in ascending order, i.e, of the output of count. No need to label the horizontal axis in this case. Use bar not hist. Save the chart in PNG format to a file named: chart2.png.


def main():
    data = read_data("data.dat")

    print(stats(data))

if __name__ == '__main__':
    main()
