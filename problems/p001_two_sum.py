"""
URL: https://leetcode.com/problems/two-sum/
DESCRIPTION:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    complements = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return complements[complement], i
        complements[num] = i
