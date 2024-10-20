#!/usr/bin/python3
"""
Module 0-minoperations
Contains method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters
    starting from a single 'H' character, using only Copy All and Paste operations.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
             Returns 0 if n is impossible to achieve.
    """
    if n < 2:
        return 0
    total_operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            total_operations += divisor
            n = n // divisor
        divisor += 1
    return total_operations
