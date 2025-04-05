# 1. Name:
#      Benjamin Black
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program reads power data from a JSON file and finds the highest average
#      power over a specified window size. Implements a sliding window algorithm
#      to calculate the max avg w/o redundant calculations.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me actually had nothing to do with the base assignment but instead writing
#      a test harness for the app like I have done in previous weeks. Then I realized the test cases
#      are so few this week that I didnt even need to write a test harness.
# 5. How long did it take for you to complete the assignment?
#      This assignment was much easier than previous weeks, It took me ~1 hour to do this Lab.

import json
import os

def find_highest_average_power(power_readings, window_size):
    """
    Find the highest average power over any window of the specified size.
    
    Args:
        power_readings (list): List of integer power readings
        window_size (int): Size of the window to calculate average over
        
    Returns:
        float: The highest average power
    """
    # Do we have enough data for the window size???
    assert len(power_readings) >= window_size, "Not enough data for the specified window size"
    
    # Calc the init window sum
    current_sum = sum(power_readings[:window_size])
    max_sum = current_sum
    
    # Slide the window
    for i in range(window_size, len(power_readings)):
        # Update cur sum
        current_sum = current_sum - power_readings[i - window_size] + power_readings[i]
        
        # Update max sum
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum / window_size

def validate_file(filename):
    """
    Validate that the file exists, is in JSON format, and contains the required data.
    
    Args:
        filename (str): Name of the file to validate
        
    Returns:
        list or None: List of power readings if valid, None otherwise
    """
    # Does it exist?
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return None
    
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not in valid JSON format.")
        return None
    except Exception as e:
        print(f"Error: Could not read file '{filename}': {str(e)}")
        return None
    
    # Valid Array?
    if "array" not in data:
        print(f"Error: File '{filename}' does not contain 'array' as a key.")
        return None
    
    # Valid Array?
    power_readings = data["array"]
    if not isinstance(power_readings, list):
        print(f"Error: The 'array' value in '{filename}' is not a list.")
        return None
    
    # Valid Array?
    for reading in power_readings:
        if not isinstance(reading, int):
            print(f"Error: The 'array' in '{filename}' contains non-integer values.")
            return None
    
    # we have at least one reading
    assert len(power_readings) > 0, "Power readings array is empty"
    
    return power_readings

def get_window_size(power_readings):
    """
    Prompt the user for a valid window size.
    
    Args:
        power_readings (list): List of power readings
        
    Returns:
        int or None: Valid window size if provided, None otherwise
    """
    try:
        window_size = int(input("Enter the size of the sub-array: "))
        
        # window valid?
        if window_size <= 0:
            print("Error: Window size must be a positive integer.")
            return None
        
        if window_size > len(power_readings):
            print(f"Error: Window size ({window_size}) cannot be larger than the number of power readings ({len(power_readings)}).")
            return None
        
        return window_size
    except ValueError:
        print("Error: Please enter a valid integer for the window size.")
        return None

def main():
    try:
        # get file
        filename = input("Enter the name of the power data file: ")
        
        # validate file
        power_readings = validate_file(filename)
        if power_readings is None:
            return
        
        # window size?
        window_size = get_window_size(power_readings)
        if window_size is None:
            return
        
        # Calculate
        try:
            highest_avg = find_highest_average_power(power_readings, window_size)
            print(f"The highest average power over a window of size {window_size} is: {highest_avg:.2f}")
        except AssertionError as e:
            print(f"Error: {e}")
            
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()