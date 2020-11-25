"""
Given a list of integers nums, return whether there's two numbers such that one is a triple of another.


"""


class Solution:
    def solve(self, nums):
        tracker = set()
        for x in nums:
            if 3 * x in tracker or x % 3 == 0 and x // 3 in tracker:
                return True
            tracker.add(x)
        return False
