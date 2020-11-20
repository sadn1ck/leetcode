"""
Given a list of integers, find the largest product of two distinct elements
"""


class Solution:
    def solve(self, nums):
        if len(nums) == 2:
            return nums[0] * nums[1]
        nums.sort()
        return max(nums[0] * nums[1], nums[-1] * nums[-2])
