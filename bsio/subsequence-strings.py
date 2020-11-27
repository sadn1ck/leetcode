"""
Given two strings s1 and s2, determine if s1 is a subsequence of s2.

A string a is a subsequence of another string b if you can delete some (or 0) characters from b, without changing the order, and get a.

For example, "ace" is a subsequence of "abcde", but "eca" is not a subsequence of "abcde".


"""


class Solution:
    def solve(self, s1, s2):
        l1 = 0
        l2 = 0
        while l1 < len(s1) and l2 < len(s2):
            # print(s1[l1], s2[l2])
            if s1[l1] == s2[l2]:
                l1 += 1
            l2 += 1
        print(l1, l2)
        if l1 == len(s1):
            return True
        return False
