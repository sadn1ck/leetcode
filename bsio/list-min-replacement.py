"""
Given a list of integers nums, replace every nums[i] with the smallest integer left of i. Replace nums[0] with 0.

"""


import math


class Solution:
    def solve(self, nums):
        mns = [0] * len(nums)
        runmin = math.inf
        for i in range(1, len(nums)):
            runmin = min(runmin, nums[i-1])
            mns[i] = runmin
        return mns
