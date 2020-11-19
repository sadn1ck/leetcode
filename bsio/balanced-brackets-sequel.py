"""
Given a string s containing round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string ([])[]({}), you should return true.

Given the string ([)] or (((), you should return false.
"""


class Solution:
    def solve(self, s):
        opening = ["[", "{", "("]
        closing = ["]", "}", ")"]
        stk = []
        cnt = 0
        for ch in s:
            # print(stk, ch, stk[-1] if len(stk) > 0 else -1)
            if ch in opening:
                stk.append(ch)
            elif ch in closing and len(stk) > 0:
                if ch == ')' and stk[-1] == '(':
                    cnt += 2
                    stk.pop()
                elif ch == ']' and stk[-1] == '[':
                    cnt += 2
                    stk.pop()
                elif ch == '}' and stk[-1] == '{':
                    cnt += 2
                    stk.pop()
                else:
                    return False
            else:
                return False
        if len(stk) > 0:
            return False
        else:
            return True
