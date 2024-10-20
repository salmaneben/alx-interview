#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = i  # Worst case: all single character additions
        
        j = 2
        while j * j <= i:
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + dp[i // j])
            j += 1
    
    return dp[n]