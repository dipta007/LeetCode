class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for v in t:
            if i < len(s) and s[i] == v:
                i += 1
        
        return i == len(s)
