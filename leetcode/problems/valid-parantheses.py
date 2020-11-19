"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif len(stack)> 0 and stack[-1] == '(' and ch == ')':
                stack.pop()
            elif len(stack)> 0 and stack[-1] == '{' and ch == '}':
                stack.pop()
            elif len(stack)> 0 and stack[-1] == '[' and ch == ']':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                
            