import io
from contextlib import redirect_stdout
from unittest.mock import patch

def run_main_with_inputs(inputs):
    with patch('builtins.input', side_effect=inputs):
        try:
            import numdays
            output_capture = io.StringIO()
            with redirect_stdout(output_capture):
                numdays.main()
            return output_capture.getvalue()
        except Exception as e:
            return f"ERROR: {str(e)}"

def demonstrate_test_cases():
    print("\n===== AUTOMATED TEST CASE DEMONSTRATIONS =====\n")
    
    test_cases = [
        {
            "name": "1. Error with year less than 1753",
            "inputs": ["1752", "1753", "10", "10", "2000", "1", "1"],
            "expected": "Error: Year must be 1753 or later"
        },
        {
            "name": "2. Error year that is not an integer",
            "inputs": ["banana", "2000", "10", "10", "2001", "1", "1"],
            "expected": "Error: Year must be an integer"
        },
        {
            "name": "3. Error month that is less than 1",
            "inputs": ["2000", "0", "1", "10", "2001", "1", "1"],
            "expected": "Error: Month must be 1 or greater"
        },
        {
            "name": "4. Error month that is greater than 12",
            "inputs": ["2000", "13", "12", "10", "2001", "1", "1"],
            "expected": "Error: Month must be 12 or less"
        },
        {
            "name": "5. Error day that is less than 1",
            "inputs": ["2000", "10", "0", "1", "2001", "1", "1"],
            "expected": "Error: Day must be 1 or greater"
        },
        {
            "name": "6. Error day greater than days in month (Feb 29, 2003)",
            "inputs": ["2003", "2", "29", "28", "2003", "3", "1"],
            "expected": "Error: 2/2003 has only 28 days"
        },
        {
            "name": "7. Error: end date before start date",
            "inputs": ["2001", "1", "9", "2001", "1", "8", "2001", "1", "10"],
            "expected": "Error: End date cannot be before start date"
        },
        {
            "name": "8. Start and end on same day (Jan 9, 2001)",
            "inputs": ["2001", "1", "9", "2001", "1", "9"],
            "expected": "There are 0 days"
        },
        {
            "name": "9. Same month/year (Jan 9-19, 2001)",
            "inputs": ["2001", "1", "9", "2001", "1", "19"],
            "expected": "There are 10 days"
        },
        {
            "name": "10. Same year (Jan 9 - Apr 19, 2001)",
            "inputs": ["2001", "1", "9", "2001", "4", "19"],
            "expected": "There are 100 days"
        },
        {
            "name": "11. Different years (Jan 9, 2001 - Oct 6, 2003)",
            "inputs": ["2001", "1", "9", "2003", "10", "6"],
            "expected": "days between"
        },
        {
            "name": "12. Leap years (Jan 9, 2001 - May 27, 2028)",
            "inputs": ["2001", "1", "9", "2028", "5", "27"],
            "expected": "days between"
        }
    ]
    
    for test_case in test_cases:
        print(f"\n{test_case['name']}")
        print("Inputs:", ", ".join(test_case["inputs"]))
        result = run_main_with_inputs(test_case["inputs"])
        print("Result:")
        print(result.strip())
        if test_case["expected"] in result:
            print("✓ PASS: Found expected output")
        else:
            print("✗ FAIL: Expected output not found")
        print("-" * 50)

if __name__ == "__main__":
    demonstrate_test_cases()