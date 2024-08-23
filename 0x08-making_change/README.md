## Making Change
Problem:
Given a set of coins with different values, determine the minimum number of coins required to achieve a given target amount.
Function Signature:
def make_change(coins, total):

Parameters:
 * coins: A list of integers representing the values of available coins.
 * total: The target amount to be reached.
Returns:
 * The minimum number of coins needed to make the total amount.
 * -1 if the total cannot be achieved using the given coins.
Notes:
 * If total is 0 or less, the function should return 0.
 * All coin values in the coins list are assumed to be positive integers.
Example Usage:
coins = [1, 2, 5]
total = 11

result = make_change(coins, total)
print(result)  # Output: 3 (using 5, 5, and 1 coins)

