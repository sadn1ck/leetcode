"""
Given a string s, consisting of "X" and "Y"s, delete the minimum number of characters 
such that there's no consecutive "X" and no consecutive "Y".

"""


class Solution:
    def solve(self, s):
        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            elif len(stack) > 0:
                if stack[-1] == ch:
                    continue
                else:
                    stack.append(ch)
        s = "".join(stack)
        return s
