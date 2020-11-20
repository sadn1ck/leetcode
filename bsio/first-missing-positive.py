"""
Given a list of integers nums, find the first missing positive integer. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.
"""


class Solution:
    def solve(self, nums):
        store = dict()
        mx = 0
        for i in nums:
            if i not in store:
                store[i] = 1
                mx = max(mx, i)
        # print(mx, store)
        for i in range(1, mx+1):
            if i not in store:
                return i
        return mx + 1
