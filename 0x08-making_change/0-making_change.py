#!/usr/bin/python3

"""
0x08-making_change
"""


def makeChange(coins, total):
    """
    Determine the min number of coins needed to make a given total.

    Parameters:
    coins (list): Coin denominations.
    total (int): Total amount of money.

    Returns:
    int: Min number of coins or -1 if not possible.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
