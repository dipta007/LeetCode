class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def call(ind):
            if ind == 1:
                return "0"
            
            v = call(ind-1)
            iv = ""
            for c in v[::-1]:
                iv += ("1" if c == "0" else "0")
            
            return v + "1" + iv

        return call(n)[k-1]