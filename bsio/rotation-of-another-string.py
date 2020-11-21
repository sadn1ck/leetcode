
"""
Given two strings s0 and s1, determine if one is a rotation of the other.


"""


class Solution:
    def solve(self, s0, s1):
        if len(s0) != len(s1):
            return False
        return s1 in s0 + s0
