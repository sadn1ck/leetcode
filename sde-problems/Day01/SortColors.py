from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(''.join([str(i) for i in nums]))
        for i in range(cnt['0']):
            nums[i] = 0
        for i in range(cnt['0'], cnt['0'] + cnt['1']):
            nums[i] = 1
        for i in range(cnt['0'] + cnt['1'], cnt['0'] + cnt['1'] + cnt['2']):
            nums[i] = 2


"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

"""
