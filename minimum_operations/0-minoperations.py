#!/usr/bin/python3
"""Minimum operations module.

This module calculates the least number of operations needed to
reach exactly n H characters using only Copy All and Paste.
"""


def minOperations(n):
    """Return the minimum number of operations to achieve n H characters.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: Minimum number of operations, or 0 if n is not attainable.
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
