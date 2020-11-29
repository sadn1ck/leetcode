"""
Write a function that rotates a list of numbers to the left by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by 2 becomes [3, 4, 5, 6, 1, 2]. Numbers should wrap around.

Note: The list is guaranteed to have at least one element, and k is guaranteed to be less than or equal to the length of the list.


"""


class Solution:
    def solve(self, nums, k):
        if k == len(nums) or k == 0:
            return nums
        else:
            if k > len(nums):
                k = k % len(nums)
            temp = nums[k:] + nums[0:k]
            return temp


class Solution2:
    def solve(self, nums, k):
        return nums[k:] + nums[:k]
