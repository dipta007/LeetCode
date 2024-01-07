class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = {}
        mark = {}
        for i in range(len(arr)-1, -1, -1):
            v = arr[i]
            
            mark[i] = 1
            if v + difference in mp:
                ind = mp[v+difference]
                mark[i] = mark[ind] + 1
            mp[v] = i 

        
        # print(mp)
        return max(mark.values())