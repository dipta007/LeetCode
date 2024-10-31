class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            i = 0
            res = []
            while i < len(s):
                j = i
                cnt = 0
                while j < len(s) and s[j] == s[i]:
                    j += 1
                    cnt += 1
                
                res.extend([cnt, s[i]])
                i = j
            
            return "".join(str(x) for x in res)

        def call(n):
            if n == 1:
                return "1"
            
            return rle(call(n-1))
        
        return call(n)