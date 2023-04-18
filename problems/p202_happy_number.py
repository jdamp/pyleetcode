"""
URL: https://leetcode.com/problems/happy-number
DESCRIPTION:
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""




def get_digit_square_sum(n: int) -> int:
    current = n
    digit_square_sum = 0
    while current > 0:
        digit = current % 10
        digit_square_sum += digit**2
        current = current//10
    return digit_square_sum


def is_happy(n: int) -> bool:
    """
    Uses Floyds cycle detection algorithm to search for
    """
    slow = get_digit_square_sum(n)
    fast = get_digit_square_sum(slow)
    while slow != fast:
        slow = get_digit_square_sum(slow)
        fast = get_digit_square_sum(fast)
        fast = get_digit_square_sum(fast)
    return slow == 1
