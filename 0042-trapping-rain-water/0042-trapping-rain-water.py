class Solution:
    def trap(self, height: List[int]) -> int:
        rgt = [0]
        for i in range(len(height)-1, -1, -1):
            rgt.append(max(rgt[-1], height[i]))
        
        rgt.reverse()
        tot = 0
        lft = 0
        for i, h in enumerate(height):
            lft = max(lft, h)
            nw = (min(lft, rgt[i]) - h)
            tot += nw

        
        return tot

# 1 2 2 2 3 3 3 3 3 3 3 3
# 0 1 0 2 1 0 1 3 2 1 2 1
# rgt
# 3 3 3 3 3 3 3 3 2 2 2 1
# lft
# 0 1 1 2 2 2 2 3 3 3 3 3
# min
# 0 1 1 2 2 2 2 3 2 2 2 1
