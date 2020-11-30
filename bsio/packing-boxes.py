"""
Given a list of integers nums, pack consecutive elements of the same value into sublists.
For example, given the list [4, 4, 1, 6, 6, 6, 1, 1, 1, 1],
return [[4, 4], [1], [6, 6, 6], [1, 1, 1, 1]].
Note: If there's only one occurrence in the list it should still be in its own sublist.


"""


from itertools import groupby


class Solution:
    def solve(self, nums):
        res = []
        temp = []
        if len(nums) == 0:
            return []
        for i in nums:
            if len(temp) > 0 and temp[-1] == i:
                temp.append(i)
                print(i)
            elif len(temp) > 0 and temp[-1] != i:
                res.append(temp)
                temp = [i]
            elif len(temp) == 0:
                temp.append(i)
        res.append(temp)
        return res


class Solution2:
    def solve(self, nums):
        return [list(y) for x, y in groupby(nums)]
