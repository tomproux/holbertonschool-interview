#!/usr/bin/python3

def makeChange(coins, total):
    """
    Function that determines the fewest number of coins
    needed to meet a given amount total.
    :param coins: list of the values of the coins in your possession
    :param total: total amount you need to make change for
    :return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Initialize a list to store
    # the minimum number of coins for each amount up to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins are needed to make change for 0

    # Iterate through each coin and update the min_coins list
    for coin in coins:
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(min_coins[amount],
                                        min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
