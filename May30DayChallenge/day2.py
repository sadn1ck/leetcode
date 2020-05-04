class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for c in J:
            cnt = cnt + S.count(c)
        return cnt
# Jewels and Stones
