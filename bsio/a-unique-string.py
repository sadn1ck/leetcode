"""
Given a string s, determine whether it has all unique characters.
"""


class Solution:
    def solve(self, s):
        return len(set(s)) == len(s)
