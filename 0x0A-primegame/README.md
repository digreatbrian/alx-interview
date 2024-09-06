Problem Statement  
Maria and Ben are playing a game. Given a sequence of consecutive integers from 1 to n, they take turns choosing a prime number. Once a prime is chosen, it and its multiples are removed from the sequence. The player who cannot make a move loses.

Task:
Given the number of rounds, x, and an array of n values for each round, determine the winner of each round assuming both players play optimally.

Input:
 * x: Number of rounds
 * nums: Array of n values for each round
Output:
 * Name of the player who won the most rounds
 * None if a winner cannot be determined
Solution Approach
 * Prime Number Counting:
   * For each round's n, count the number of prime numbers in the range from 1 to n.
 * Winner Determination:
   * If the number of primes is odd, Maria wins.
   * If the number of primes is even, Ben wins.
 * Overall Winner:
   * Track the wins for each player across all rounds.
   * Return the player with the most wins. If there's a tie, return None.
Edge Cases
 * If x is 0 or None, return None.
 * If nums is None or empty, return None.

