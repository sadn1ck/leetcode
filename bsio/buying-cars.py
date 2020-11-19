"""
Given a list of integers prices representing prices of cars for sale, and a budget k, return the maximum number of cars you can buy.
"""


class Solution:
    def solve(self, prices, k):
        prices.sort()
        cnt = 0
        i = 0
        if k == 0:
            return 0
        for i, v in enumerate(prices):
            k = k - v
            # print(k, i)
            if k == 0:
                return i + 1
            elif k < 0:
                return i
        return len(prices)
