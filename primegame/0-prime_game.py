#!/usr/bin/python3
"""Prime Game implementation."""


def isWinner(x, nums):
    """Return the name of the player that won the most rounds.

    The game on the interval [1, n] is fully determined by the number of
    prime integers in that interval. Each move removes exactly one prime and
    its non-prime multiples, so the number of moves is just the number of
    primes less than or equal to n.
    """
    if x <= 0 or not nums:
        return None

    limit = max(nums)
    sieve = [True] * (limit + 1)

    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False

    for number in range(2, int(limit ** 0.5) + 1):
        if sieve[number]:
            for multiple in range(number * number, limit + 1, number):
                sieve[multiple] = False

    prime_counts = [0] * (limit + 1)
    prime_total = 0
    for number in range(limit + 1):
        if sieve[number]:
            prime_total += 1
        prime_counts[number] = prime_total

    maria_wins = 0
    ben_wins = 0

    for index in range(x):
        if index >= len(nums):
            break
        if prime_counts[nums[index]] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    if maria_wins > ben_wins:
        return "Maria"
    return "Ben"
