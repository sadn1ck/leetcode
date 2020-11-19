"""
Given a list of strings strs, containing the strings "red", "green" and "blue", partition the list so that the red come before green, which come before blue.


"""


class Solution:
    def solve(self, strs):
        count = {"red": 0, "green": 0, "blue": 0}
        for st in strs:
            count[st] += 1
        arr = ["red"] * count["red"] + ["green"] * \
            count["green"] + ["blue"] * count["blue"]
        return arr
