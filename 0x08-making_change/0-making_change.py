#!/usr/bin/python3

"""
0x08 Make changes

Calculate the minimum number of cins to make a specific total amount
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins to make a specific total amount.

    This function uses dynamic programming to find the fewest number of coins
    required to make up a given total value using available coin denominations.
    It assumes an unlimited supply of each coin type.

    Args:
        coins (list): A list of available coin denominations (positive int).
        total (int): The target total amount to make change for.

    Returns:
        int: The minimum number of coins needed to make the total amount.
             Returns 0 if total is 0 or negative.
             Returns -1 if it's impossible to make the total with given coins.
    """
    # If total is 0 or negative, return 0
    if total <= 0:
        return 0

    # Initialize DP array with a large value (total + 1 serves as infinity)
    # We use total+1 as it's always larger than any valid coin combination
    dp = [total + 1] * (total + 1)

    # Base case: 0 coins needed to make 0
    dp[0] = 0

    # Iterate through all possible totals from 1 to total
    for i in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If the coin value is less than or equal to current total
            if coin <= i:
                # Update minimum number of coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still total+1, no solution exists
    return dp[total] if dp[total] != total + 1 else -1
