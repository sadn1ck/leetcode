"""
Given a string s and an integer n, split up s into n-sized pieces.

For example, given:

s = "abcdefg"
n = 3
Return ["abc", "def", "g"].


"""


class Solution:
    def solve(self, s, n):
        chonks = []
        ln = len(s)
        for i in range(0, ln, n):
            if ln - i - 1 >= n:
                chonks.append(s[i:i+n])
            else:
                chonks.append(s[i:])
        return chonks
