"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and list(set(nums))[0] == 1:
            return len(nums) - 1
        sums = []
        cnt = 0
        for ind, i in enumerate(nums):
            if i == 0:
                sums.append(cnt)
                cnt = 0
            else:
                cnt += 1
        mx = 0
        if cnt > 0:
            sums.append(cnt)
        print(sums, cnt)
        for i in range(len(sums) - 1):
            mx = max(mx, sums[i+1] + sums[i])
        return mx
