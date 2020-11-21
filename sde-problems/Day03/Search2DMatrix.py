"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""
from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        r = len(nums)
        if r == 0:
            return False
        c = len(nums[0])
        if c == 0:
            return False
        for i in range(r):
            if nums[i][0] <= target <= nums[i][c-1]:
                x = bisect_left(nums[i], target)
                if x != c and nums[i][x] == target:
                    return True
        return False
