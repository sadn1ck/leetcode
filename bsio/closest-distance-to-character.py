"""
Given a string s and a character c, return a new list of integers of the same length as s 
where for each index i its value is set the closest distance of s[i] to c. You can assume c exists in s.
"""


class Solution:
    def solve(self, s, c):
        pos = [i for i, v in enumerate(s) if v == c][::-1]
        first = pos[0]
        second = pos.pop()
        res = []
        for i in range(len(s)):
            dis1 = abs(i - first)
            dis2 = abs(i - second)
            if dis1 < dis2:
                res.append(dis1)
            else:
                res.append(dis2)
                first = second
                if dis1 == 0 or dis2 == 0:
                    first = second
                    if len(pos) > 0:
                        second = pos.pop()

        return res
