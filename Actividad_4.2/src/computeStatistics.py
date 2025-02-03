import time

start_time = time.time()

print("Enter the file name you want to analize: ")
file_input  = str(input())

with open(f"../files/P1/{file_input}.txt", "r") as file:
    number_list = []
    for line in file:
        try:
            number = float(line.strip())
            number_list.append(number)
        except ValueError as e:
            print(f"Non recognized number '{line.strip()}': {e}")

def mean_calculation(number_list):
    """
    This Function calculates the mean value of an input list
    """
    return sum(number_list) / len(number_list)

def median_calculation(number_list):
    """
    This function calculates the median value of an input list.
    """
    sorted_list = sorted(number_list)
    list_lenght = len(sorted_list)
    mid_value = list_lenght // 2

    if list_lenght % 2 == 1: 
        return sorted_list[mid_value]
    else:  
        return (sorted_list[mid_value - 1] + sorted_list[mid_value]) / 2

def mode_calculation(number_list):
    """
    This function calculates the mode value of an input list.
    """
    freq = {}
    for num in number_list:
        freq[num] = freq.get(num, 0) + 1
    
    max_freq = max(freq.values())  
    modes = [key for key, value in freq.items() if value == max_freq]

    return modes

def variance_calculation(number_list):
    """
    This function calculates the variance value of an input list.
    """
    mean_value = mean_calculation(number_list)
    squared_diffs = [(x - mean_value) ** 2 for x in number_list]
    
    return sum(squared_diffs) / len(number_list)  

def standard_deviation_calcualtion(number_list):
    """
    This function calculates the standard deviation of an input list.
    """
    return variance_calculation(number_list) ** 0.5

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

file_path = "../outputs/P1/output.txt"  

with open(file_path, "a") as file:
    file.write("\n\n" + file_input + "\n\n")
    
    # Write the dictionary in a readable format
    for key, value in statistical_outputs.items():
        file.write(f"{key}: {value}\n")

print(f"Data successfully saved to {file_path}")
print(f"Time elapsed for execution and data calculation: {elapsed_time:.4f} seconds")