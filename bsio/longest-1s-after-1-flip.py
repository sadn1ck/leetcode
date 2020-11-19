"""
You are given a string s containing 1s and 0s.
 Given that you can flip at most one "0", return the length of the longest contiguous substring of 1s
"""


class Solution:
    def solve(self, s):
        c1 = []
        cnt = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(set(list(s))) == 1 and list(set(list(s)))[0] == '1':
            return len(s)
        for ch in s:
            if ch == '1':
                cnt += 1
            elif ch == '0':
                c1.append(cnt)
                cnt = 0
        c1.append(cnt)
        mx = 0
        for i in range(len(c1) - 1):
            mx = max(c1[i] + c1[i+1], mx)
        return mx + 1
