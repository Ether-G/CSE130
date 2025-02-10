# 1. Name:
#      Benjamin Black
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program implements an advanced binary search algorithm that efficiently
#      searches for a string in a sorted list of strings stored in a JSON file.
#      The program prompts for a filename and search term, then reports whether
#      the term was found using binary search comparison.
# 4. Algorithmic Efficiency:
#      O(log n) - The binary search algorithm divides the search space in half with
#      each iteration. For n strings in the list, it performs at most log2(n) string
#      comparisons. String comparisons are lexicographical (dictionary order).
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part for me was initially figuring out how to apply the binary search
#      algorithm we came up with to sorted lists of strings. But then I remembered that
#      letters are base 26 numbers, I just need to id the base, then sort based on where it
#      places in its base.
# 6. How long did it take for you to complete the assignment?
#      It took ~60 mins.

import json

def binary_search(sorted_list, target):
    """
    Perform binary search to find target string in sorted_list.
    Returns True if found, False otherwise.
    
    Sorted in alphabetical order.

    I looked up the standard python rules for this:
    - 'A' < 'B' (uppercase before lowercase)
    - 'a' < 'b' (alphabetical order)
    - 'C++' < 'Java' (character by character comparison)
    """
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        # Compare strings
        if sorted_list[middle] == target:
            return True
        elif sorted_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
            
    return False

def main():
    # Get filename
    filename = input("What is the name of the file? ")
    
    try:
        # Read JSON
        with open(filename, 'r') as file:
            data = json.load(file)
            array = data.get("array", [])
        
        # Get search term
        search_term = input("What name are we looking for? ")
        
        # search and results
        if binary_search(array, search_term):
            print(f"We found {search_term} in {filename}.")
        else:
            print(f"We could not find {search_term} in {filename}.")
            
    except FileNotFoundError:
        print(f"Unable to open {filename}. Please verify the file exists.")
    except json.JSONDecodeError:
        print(f"Error: {filename} does not contain valid JSON data.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()