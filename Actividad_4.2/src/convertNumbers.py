"""
This is the documentation part
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
            number = int(line.strip())
            number_list.append(number)
        except ValueError as e:
            print(f"Non recognized number '{line.strip()}': {e}")

def decimal_to_binary_transformer(_number_list):
    """
    This function calculates the conversion from a decimal number to a
    binary number with an extra bit for negative numbers that represnts the sign
    """
    binary_list = []

    for n in number_list:
        if n == 0:
            binary_list.append("0")
            continue

        if n < 0:
            binary = ""
            num = abs(n)

            while num > 0:
                binary = str(num % 2) + binary
                num //= 2

            binary = "1" + binary
        else:
            binary = ""
            num = n

            while num > 0:
                binary = str(num % 2) + binary
                num //= 2

        binary_list.append(binary)

    return binary_list


def decimal_to_hexadecimal_transformer(_number_list):
    """
    This function calculates the conversion from a decimal number to a
    hexadecimal number
    """

    hex_chars = "0123456789ABCDEF"
    hex_list = []

    for n in _number_list:
        if n == 0:
            hex_list.append("0")
            continue

        hex_value = ""

        is_negative = n < 0
        if is_negative:
            n = abs(n)

        while n > 0:
            hex_value = hex_chars[n % 16] + hex_value
            n //= 16

        if is_negative:
            hex_value = "-" + hex_value

        hex_list.append(hex_value)

    return hex_list

binary_number_list = decimal_to_binary_transformer(number_list)
hexa_number_list = decimal_to_hexadecimal_transformer(number_list)

transformed_combined_list = list(zip(number_list, binary_number_list, hexa_number_list))

end_time = time.time()
elapsed_time = end_time - start_time

for row in transformed_combined_list:
    for value in row:
        print(value)
    print("-" * 10)

PATH = "../outputs/P2/ConvertionResults.txt"

with open(PATH, "a", encoding = "UTF-8") as file:
    file.write("\n\n" + file_input + "\n\n")
    file.write(f"Time elapsed for execution & data calculation: {elapsed_time:.4f} seconds" + "\n")

    for row in transformed_combined_list:
        for value in row:
            file.write(str(value) + "\n")
        file.write("-" * 10 + "\n")

print(f"Data successfully saved to {PATH}")
print(f"Time elapsed for execution and data calculation: {elapsed_time:.4f} seconds")
