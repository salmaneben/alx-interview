#!/usr/bin/python3
"""
Module 0-minoperations
Contains a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters
    starting from a single 'H', using only Copy All and Paste operations.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
             Returns 0 if n is impossible to achieve.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    total_operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            total_operations += divisor
            n //= divisor
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                total_operations += n
            break

    return total_operations
