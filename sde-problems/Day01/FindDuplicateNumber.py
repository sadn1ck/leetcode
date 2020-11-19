from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = set()
        for i in nums:
            if i in store:
                return i
            store.add(i)
        return -1


"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.
"""
