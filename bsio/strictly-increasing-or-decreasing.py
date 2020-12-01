"""
Given an list of numbers, determine whether the list is strictly increasing or strictly decreasing.


"""


class Solution:
    def solve(self, nums):
        inc = 0
        dec = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                inc = -1
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                dec = -1
        if inc == 0 or dec == 0:
            return True
        else:
            return False
