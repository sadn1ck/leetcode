"""
Given a list of integers nums, return a new list such that 
each element at index i of the new list is the product of all the numbers in the original list except the one at i.

 Do this without using division.
"""


class Solution:
    def solve(self, nums):
        front = []
        back = []
        prod = 1
        for i in nums:
            prod = prod * i
            front.append(prod)
        prod = 1
        for i in nums[::-1]:
            prod = prod * i
            back.append(prod)
        back = back[::-1]
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(back[i+1])
            elif i == len(nums) - 1:
                res.append(front[i-1])
            else:
                res.append(front[i-1] * back[i+1])
        return res
