#!/usr/bin/python3
"""
Making Change, the minimum number of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total.

    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met

    Returns:
        int: Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if total >= coin:
            coin_count += total // coin
            total %= coin

    if total != 0:
        return -1

    return coin_count
