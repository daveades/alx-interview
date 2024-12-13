#!/usr/bin/python3

"""
0x08-making_change
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given amount `total`.

    Args:
        coins (list): A list of the values of the coins available.
        total (int): The total amount of money to make change for.

    Returns:
        int: The minimum number of coins needed to make the change for the given `total`.
             If the change cannot be made with the given coins, return -1.
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)

    def helper(t):
        if t == 0:
            return 0
        min_coins = float('inf')
        for coin in coins:
            if t >= coin:
                res = helper(t - coin)
                if res != -1 and res + 1 < min_coins:
                    min_coins = res + 1
        return min_coins if min_coins != float('inf') else -1

    return helper(total)
