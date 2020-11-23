"""
Given a sorted list of integers, square the elements and give the output in sorted order.

Note: The integers can be 0 or negative.
"""


class Solution:
    def solve(self, nums):
        return sorted([x**2 for x in nums])
