"""
This script calculates basic statistical metrics from a given input file.

It reads a list of numbers from a file (provided as a command-line argument), 
performs statistical calculations (mean, median, mode, variance, and standard deviation), 
and saves the results to an output file.

Usage:
    python script.py <input_file>

Where:
    - <input_file> should be a text file containing one number per line.

The script performs the following steps:
1. Reads and validates the input file.
2. Extracts numeric values, ignoring non-numeric lines.
3. Computes statistical measures:
    - Mean
    - Median
    - Mode
    - Variance
    - Standard Deviation
4. Saves results in `../outputs/P1/StatisticsResults.txt`.
5. Prints the computed values and execution time.

Functions:
    - mean_calculation(number_list): Computes the mean of the given list.
    - median_calculation(number_list): Computes the median of the given list.
    - mode_calculation(number_list): Computes the mode of the given list.
    - variance_calculation(number_list): Computes the variance of the given list.
    - standard_deviation_calculation(number_list): Computes the standard deviation of a given list.

Exceptions:
    - Raises FileNotFoundError if the input file is missing.
    - Ignores non-numeric lines and prints a warning.

Output:
    The script prints the calculated statistics and saves them in a text file.

Author: [Alonso Pedrero]
Date: [03-01-2025]
"""

import pathlib
import sys
import time

start_time = time.time()

file_input  = sys.argv[1]

if not pathlib.Path(file_input).is_file():
    raise FileNotFoundError("File not found: ", file_input)

print("Found file:", file_input)

with open(file_input, "r", encoding = "UTF-8") as file:
    number_list = []
    for line in file:
        try:
            number = float(line.strip())
            number_list.append(number)
        except ValueError as e:
            print(f"Non recognized number '{line.strip()}': {e}")

def mean_calculation(_number_list):
    """
    This Function calculates the mean value of an input list
    """
    return sum(_number_list) / len(_number_list)

def median_calculation(_number_list):
    """
    This function calculates the median value of an input list.
    """
    sorted_list = sorted(_number_list)
    list_lenght = len(sorted_list)
    mid_value = list_lenght // 2

    if list_lenght % 2 == 1:
        return sorted_list[mid_value]

    return (sorted_list[mid_value - 1] + sorted_list[mid_value]) / 2

def mode_calculation(_number_list):
    """
    This function calculates the mode value of an input list.
    """
    freq = {}
    for num in _number_list:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())
    modes = [key for key, value in freq.items() if value == max_freq]

    if len(modes) == len(_number_list):
        return "#N/A"

    return modes

def variance_calculation(_number_list):
    """
    This function calculates the variance value of an input list.
    """
    mean_value = mean_calculation(_number_list)
    squared_diffs = [(x - mean_value) ** 2 for x in _number_list]

    return sum(squared_diffs) / len(_number_list)

def standard_deviation_calcualtion(_number_list):
    """
    This function calculates the standard deviation of an input list.
    """
    return variance_calculation(_number_list) ** 0.5

avg = mean_calculation(number_list)
median = median_calculation(number_list)
mode = mode_calculation(number_list)
variance = variance_calculation(number_list)
sdv = standard_deviation_calcualtion(number_list)
end_time = time.time()
elapsed_time = end_time - start_time

statistical_outputs = {
    "Mean" : avg,
    "Median" : median,
    "Mode" : mode,
    "Variance" : variance,
    "SD" : sdv,
    "Time" : elapsed_time
}

print(statistical_outputs)

PATH = "../outputs/P1/StatisticsResults.txt"

with open(PATH, "a", encoding = "UTF-8") as file:
    file.write("\n\n" + file_input + "\n\n")

    for key, value in statistical_outputs.items():
        file.write(f"{key}: {value}\n")

print(f"Data successfully saved to {PATH}")
print(f"Time elapsed for execution and data calculation: {elapsed_time:.4f} seconds")
