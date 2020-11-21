"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occ = {}
        times = (len(nums))//2
        for n in nums:
            if n not in occ:
                occ[n] = 1
            else:
                occ[n] += 1
        out = []
        # print(times)
        for i in occ:
            if occ[i] > times:
                out.append(i)
        return out[0]
