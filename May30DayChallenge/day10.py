class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        p = {}
        # dictionary to store how many people trust i
        # N = 4
        for i in range(1, N+1):
            p[i] = 0
        # print(p)
        for pair in trust:
            # pair[0] trusts pair[1]
            a = pair[0]
            b = pair[1]
            p[a] -= 1
            p[b] += 1
            
        for i in range(1, N+1):
            if p[i] == N-1:
                return i
        return -1
            