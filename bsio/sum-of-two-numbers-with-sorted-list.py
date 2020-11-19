"""
Given a list of integers nums sorted in ascending order and an integer k, 
return whether any two numbers from the list add up to k. 
You may not use the same element twice.
"""


class Solution:
    def solve(self, nums, k):
        l = 0
        r = len(nums) - 1
        nums.sort()
        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                return True
        return False
