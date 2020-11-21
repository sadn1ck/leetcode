"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for i in range(1, len(nums)):
            x = x ^ nums[i]
        return x
