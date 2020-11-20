"""
Given a sorted unique integer list of size n in increasing order, find the first positive integer between [1, n+1] not in the array.

"""


class Solution:
    def solve(self, arr):
        n = len(arr) + 1
        unique = set(arr)
        print(n)

        for value in range(1, n):
            if value not in unique:
                return value
        return arr[-1] + 1
