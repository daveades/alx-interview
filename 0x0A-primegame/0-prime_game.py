#!/usr/bin/python3
"""
0x0A - Prime Game
Module to determine the winner of the Prime Game.
"""


def isWinner(x, nums):
    """Determine winner of Prime Game"""
    if not nums or x < 1 or len(nums) != x:
        return None

    # Pre-calculate primes up to max number for efficiency
    # Sieve of Eratosthenes
    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count primes up to n using pre-calculated sieve
        prime_count = sum(1 for i in range(2, n + 1) if sieve[i])
        # Even number of primes means Ben wins, odd means Maria wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
