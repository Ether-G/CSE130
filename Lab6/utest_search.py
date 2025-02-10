import unittest
import json
from search import binary_search

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        """Load all test files before running tests"""
        # Load empty file
        with open('Lab06.empty.json', 'r') as file:
            self.empty_data = json.load(file)['array']
            
        # Load trivial file
        with open('Lab06.trivial.json', 'r') as file:
            self.trivial_data = json.load(file)['array']
            
        # Load languages file
        with open('Lab06.languages.json', 'r') as file:
            self.languages_data = json.load(file)['array']
            
        # Load countries file
        with open('Lab06.countries.json', 'r') as file:
            self.countries_data = json.load(file)['array']

    def test_empty_list(self):
        """Testing empty list (Lab06.empty.json)"""
        test_term = "Empty"
        print(f"\nTesting empty list search for '{test_term}'")
        print(f"List contents: {self.empty_data}")
        result = binary_search(self.empty_data, test_term)
        print(f"Search result: {result} (Expected: False)")
        self.assertFalse(result)
        
    def test_trivial_list_found(self):
        """Testing single item list - item exists (Lab06.trivial.json)"""
        test_term = "trivial"
        print(f"\nTesting trivial list search for '{test_term}'")
        print(f"List contents: {self.trivial_data}")
        result = binary_search(self.trivial_data, test_term)
        print(f"Search result: {result} (Expected: True)")
        self.assertTrue(result)
        
    def test_trivial_list_not_found(self):
        """Testing single item list - item doesn't exist (Lab06.trivial.json)"""
        test_term = "missing"
        print(f"\nTesting trivial list search for '{test_term}'")
        print(f"List contents: {self.trivial_data}")
        result = binary_search(self.trivial_data, test_term)
        print(f"Search result: {result} (Expected: False)")
        self.assertFalse(result)
        
    def test_languages_list_found(self):
        """Testing small list - items exist (Lab06.languages.json)"""
        test_cases = ["C++", "Python", "VB", "C"]
        print(f"\nTesting languages list")
        print(f"List contents: {self.languages_data}")
        for test_term in test_cases:
            print(f"\nSearching for '{test_term}'")
            result = binary_search(self.languages_data, test_term)
            print(f"Search result: {result} (Expected: True)")
            self.assertTrue(result)
        
    def test_languages_list_not_found(self):
        """Testing small list - items don't exist (Lab06.languages.json)"""
        test_cases = ["Lisp", "Ruby"]
        print(f"\nTesting languages list")
        print(f"List contents: {self.languages_data}")
        for test_term in test_cases:
            print(f"\nSearching for '{test_term}'")
            result = binary_search(self.languages_data, test_term)
            print(f"Search result: {result} (Expected: False)")
            self.assertFalse(result)
        
    def test_countries_list_found(self):
        """Testing large list - items exist (Lab06.countries.json)"""
        test_cases = ["United States of America", "Japan", "Afghanistan", "Zimbabwe"]
        print(f"\nTesting countries list")
        print(f"List length: {len(self.countries_data)} countries")
        for test_term in test_cases:
            print(f"\nSearching for '{test_term}'")
            result = binary_search(self.countries_data, test_term)
            print(f"Search result: {result} (Expected: True)")
            self.assertTrue(result)
        
    def test_countries_list_not_found(self):
        """Testing large list - items don't exist (Lab06.countries.json)"""
        test_cases = ["United States", "Atlantis"]
        print(f"\nTesting countries list")
        print(f"List length: {len(self.countries_data)} countries")
        for test_term in test_cases:
            print(f"\nSearching for '{test_term}'")
            result = binary_search(self.countries_data, test_term)
            print(f"Search result: {result} (Expected: False)")
            self.assertFalse(result)
        
    def test_case_sensitivity(self):
        """Testing case sensitivity in searches"""
        test_cases = [("python", "Python"), ("JAVA", "Java")]
        print(f"\nTesting case sensitivity")
        for incorrect, correct in test_cases:
            print(f"\nSearching for '{incorrect}' (correct form is '{correct}')")
            result = binary_search(self.languages_data, incorrect)
            print(f"Search result: {result} (Expected: False)")
            self.assertFalse(result)
        
    def test_exact_match(self):
        """Testing exact string matching"""
        test_cases = [("Java ", "Java"), ("C++.", "C++")]
        print(f"\nTesting exact string matching")
        for incorrect, correct in test_cases:
            print(f"\nSearching for '{incorrect}' (correct form is '{correct}')")
            result = binary_search(self.languages_data, incorrect)
            print(f"Search result: {result} (Expected: False)")
            self.assertFalse(result)

if __name__ == '__main__':
    print("Starting Binary Search Tests...\n")
    unittest.main(verbosity=2)