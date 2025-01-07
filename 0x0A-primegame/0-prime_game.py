#!/usr/bin/python3
"""
Module for Prime Game
"""


def is_prime(n):
    """
    Check if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(n):
    """
    Get list of primes up to n using Sieve of Eratosthenes
    """
    if n < 2:
        return []
    
    # Initialize sieve array
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # Apply sieve
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    # Get prime numbers
    return [i for i in range(2, n + 1) if sieve[i]]


def isWinner(x, nums):
    """
    Determine winner of Prime Game
    
    Args:
        x (int): number of rounds
        nums (list): array of n for each round
    
    Returns:
        str: name of winner (Maria/Ben) or None if cant be determined
    """
    if not nums or x < 1:
        return None
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        # Get the number of prime numbers up to n
        primes = get_primes_up_to(n)
        # If number of primes is even, Ben wins
        # If number of primes is odd, Maria wins
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None