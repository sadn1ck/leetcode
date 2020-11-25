"""
You're given a string s consisting solely of "(" and ")". Return whether the parentheses are balanced.


"""


class Solution:
    def solve(self, s):
        cnt = 0
        for ch in s:
            if ch == '(':
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    return False
        if cnt == 0:
            return True
        return False
