#!/usr/bin/python3

"""
0x0A - Prime Game
"""


def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(n):
    """Get all prime numbers up to n"""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def play_round(n):
    """Simulate a single round"""
    if n < 2:
        return 'Ben'  # Maria can't make first move

    # Get prime numbers up to n
    primes = get_primes_up_to(n)

    # If even number of moves possible, Ben wins
    # If odd number of moves possible, Maria wins
    return 'Ben' if len(primes) % 2 == 0 else 'Maria'

def isWinner(x, nums):
    """Determine winner of Prime Game"""
    if not nums or x < 1 or len(nums) != x:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
