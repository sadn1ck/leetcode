import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningsum = 0
        mx = -math.inf
        for i in nums:
            runningsum += i
            if mx < runningsum:
                mx = runningsum
            if runningsum < 0:
                runningsum = 0
        return mx


"""
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and 
return its sum.
"""
