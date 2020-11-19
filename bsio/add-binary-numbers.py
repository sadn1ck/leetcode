"""
Given two strings a and b that represent binary numbers, add them and return their sum, also as a string.

The input strings are guaranteed to be non-empty and contain only 1s and 0s.


"""


class Solution:
    def solve(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        s = x + y
        return str(bin(s)[2:])
