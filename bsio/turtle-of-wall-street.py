"""
You are given a list of integers nums representing stock prices of a company in chronological order. 
You can buy at most one share of stock per day, but you can hold onto multiple stocks and can sell stocks on any number of days. 
Return the maximum profit you can earn.
"""


class Solution:
    def solve(self, nums):
        mx = 0
        p = 0
        for i in range(len(nums) - 1, -1, -1):
            mx = max(mx, nums[i])
            p += (mx - nums[i])
        return p
