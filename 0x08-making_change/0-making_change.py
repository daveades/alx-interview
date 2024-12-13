#!/usr/bin/python3

"""
0x08-making_change
"""

def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to make a given total.

    Parameters:
    coins (list): A list of coin denominations.
    total (int): The total amount of money to make.

    Returns:
    int: The minimum number of coins needed to make the total, or -1 if it is not possible.
    """
    if total < 0:
        return 0
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    result = min_coins[total]
    return result if result != float('inf') else -1