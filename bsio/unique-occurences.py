"""
Given a list of integers nums, return whether the number of occurrences of every value in the array is unique.

Note: Numbers can be negative.
"""


class Solution:
    def solve(self, nums):
        store = {}
        for i in nums:
            if i not in store:
                store[i] = 1
            else:
                store[i] += 1
        return (len(store.values()) == len(set(store.values())))
