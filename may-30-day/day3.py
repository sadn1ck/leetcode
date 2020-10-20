from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool: 
        r = Counter(ransomNote)
        m = Counter(magazine)
        for i in r:
            print(r[i])
            if r[i] > m[i]:
                return False
        return True

# Ransom note
