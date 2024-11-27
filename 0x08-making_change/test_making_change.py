#!/usr/bin/python3
"""
Test file for finding errors in making change solution
"""
from making_change import makeChange


def test_cases():
    """Run multiple test cases and print results"""
    tests = [
        # Basic test cases from the problem
        ([1, 2, 25], 37, 7),
        ([1256, 54, 48, 16, 102], 1453, -1),
        
        # Edge cases
        ([], 0, 0),
        ([1], 0, 0),
        ([1], -1, 0),
        ([], 5, -1),
        ([2], 3, -1),
        ([1], 1, 1),
        
        # Additional test cases
        ([1, 5, 10], 7, 3),
        ([2, 5, 10, 20, 50], 98, 7),
        ([1, 2, 5], 11, 3),
        ([2, 5, 10], 3, -1),
        ([186, 419, 83, 408], 6249, -1)
    ]

    passed = 0
    failed = 0

    for coins, total, expected in tests:
        result = makeChange(coins, total)
        print(f"\nTest: coins={coins}, total={total}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        
        if result == expected:
            print("✓ PASSED")
            passed += 1
        else:
            print("✗ FAILED")
            failed += 1

    print(f"\nTest Summary:")
    print(f"Total Tests: {len(tests)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    test_cases()