"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occ = {}
        times = (len(nums))//3
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
        return out
