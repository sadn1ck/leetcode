"""
Given a string s containing brackets "(" and ")", return the length of the longest subsequence of balanced brackets.
"""


class Solution:
    def solve(self, s):
        cnt = 0
        stack = []
        if len(set(s)) == 1:
            return 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if ch == ')' and len(stack) > 0 and stack[-1] == '(':
                    cnt += 2
                    stack.pop()
            # print(stack, ch)
        return cnt
