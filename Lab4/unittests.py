import io
import sys
from contextlib import contextmanager
from typing import List, Dict

import monopoly

@contextmanager
def simulate_input(inputs: List[str]):
    """Simulate user input for testing"""
    old_stdin = sys.stdin
    input_stream = io.StringIO('\n'.join(inputs))
    sys.stdin = input_stream
    try:
        yield
    finally:
        sys.stdin = old_stdin

@contextmanager
def capture_output():
    """Capture stdout for testing"""
    old_stdout = sys.stdout
    output_stream = io.StringIO()
    sys.stdout = output_stream
    try:
        yield output_stream
    finally:
        sys.stdout = old_stdout

def run_test_case(name: str, inputs: List[str]) -> str:
    """Run a single test case and return the output"""
    with simulate_input(inputs), capture_output() as output:
        monopoly.main()
    return output.getvalue()

def print_test_result(name: str, output: str, expected_substring: str):
    """Print the results of a test case"""
    print(f"\n{'='*60}")
    print(f"Test Case: {name}")
    print(f"{'='*60}")
    print("Input values:")
    print(f"  {' | '.join(test_cases[name]['inputs'])}")
    print("\nOutput:")
    print(output.strip())
    if expected_substring.lower() in output.lower():
        print("\n✅ TEST PASSED")
    else:
        print("\n❌ TEST FAILED")
        print(f"Expected to find: {expected_substring}")

# Define all test cases
test_cases = {
    "Does not own enough": {
        "inputs": ["n", "0", "0", "0", "10", "10", "1000"],
        "expected": "cannot purchase a hotel until you own"
    },
    "Poor": {
        "inputs": ["y", "0", "0", "0", "15", "10", "100"],
        "expected": "do not have sufficient funds"
    },
    "No houses": {
        "inputs": ["y", "0", "0", "0", "0", "10", "9000"],
        "expected": "not enough houses available"
    },
    "Swap with Pacific": {
        "inputs": ["y", "4", "5", "4", "0", "0", "0"],
        "expected": "Swap Pacific's hotel"
    },
    "Swap with NC": {
        "inputs": ["y", "4", "4", "5", "0", "0", "0"],
        "expected": "Swap North Carolina's hotel"
    },
    "Already built": {
        "inputs": ["y", "5", "4", "4", "10", "10", "1000"],
        "expected": "cannot purchase a hotel if the property already has one"
    },
    "All at once": {
        "inputs": ["y", "0", "0", "0", "12", "3", "3000"],
        "expected": "This will cost"
    },
    "House and hotel": {
        "inputs": ["y", "3", "3", "3", "3", "1", "5000"],
        "expected": "This will cost"
    }
}

def run_all_tests():
    """Run all test cases"""
    print("Starting Monopoly Program Test Suite")
    print("Running all test cases...\n")
    
    for name, case in test_cases.items():
        output = run_test_case(name, case["inputs"])
        print_test_result(name, output, case["expected"])

if __name__ == "__main__":
    run_all_tests()