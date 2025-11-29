from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        count = defaultdict(int)

        low = 0
        for high in range(len(s)):
            curr_c = s[high]
            count[curr_c] += 1
            while count[curr_c] > 1:
                count[s[low]] -= 1
                low += 1
            
            res = max(res, high - low + 1)
        
        return res

        