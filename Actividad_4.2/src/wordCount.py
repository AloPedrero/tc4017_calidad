"""
Module for counting word frequencies in a text file.

This script reads a file specified as a command-line argument, counts the 
frequency of each word, sorts the results in descending order, and saves the 
output to a specified file. The execution time is also recorded.

Usage:
    python script.py <file_path>

Functions:
    frequency_calculation(_words_list): Computes the frequency of words in a list.

Output:
    - Prints the found file name and execution time.
    - Saves the sorted word count and execution time to '../outputs/P3/WordCountResults.txt'.

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
    words_list = []
    for line in file:
        try:
            WORD = str(line.strip())
            words_list.append(WORD)
        except ValueError as e:
            print(f"Non recognized word '{line.strip()}': {e}")

def frequency_calculation(_words_list):
    """
    This function calculates the frequency of the words with
    a dictionary where if the world already exist it sums a 1
    in the respective value, and if not it assigns a number 1. 
    """
    _frequency_dictionary = {}

    for word in _words_list:

        if f"{word}" in _frequency_dictionary:
            _frequency_dictionary[f"{word}"] += 1

        else:
            _frequency_dictionary[f"{word}"] = 1

    return _frequency_dictionary

frequency_dictionary = frequency_calculation(words_list)
sorted_dict = dict(sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=True))

end_time = time.time()
elapsed_time = end_time - start_time

PATH = "../outputs/P3/WordCountResults.txt"

with open(PATH, "a", encoding = "UTF-8") as file:
    file.write("\n\n" + file_input + "\n\n")
    file.write(f"Time elapsed for execution & data calculation: {elapsed_time:.4f} seconds" + "\n")

    for key, value in sorted_dict.items():
        file.write(f"{key}: {value}\n")

print(f"Data successfully saved to {PATH}")
print(f"Time elapsed for execution and data calculation: {elapsed_time:.4f} seconds")
print(sorted_dict)
