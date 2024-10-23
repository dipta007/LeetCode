class Solution:

    def __init__(self, w: List[int]):
        self.pre = [0]
        for v in w:
            self.pre.append(self.pre[-1] + v)
        print(self.pre)

    def pickIndex(self) -> int:
        # ww = random.randint(min(1, self.pre[1]), self.pre[-1]+1)
        # ww = random.randint(0, self.pre[-1]+1)
        ww = self.pre[-1] * random.random()
        # print(ww)
        l, h = 1, len(self.pre) - 1
        res = 1
        while l <= h:
            m = (l + h) // 2
            if ww <= self.pre[m]:
                res = m
                h = m - 1
            else:
                l = m + 1
        return res - 1

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()