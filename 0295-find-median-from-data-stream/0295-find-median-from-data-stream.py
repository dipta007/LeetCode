import heapq

class MedianFinder:

    def __init__(self):
        self.mn_hp = []
        self.mx_hp = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.mx_hp, -num)
        mx = -heapq.heappop(self.mx_hp)
        heapq.heappush(self.mn_hp, mx)

        if len(self.mn_hp) - len(self.mx_hp) >= 2:
            mn = heapq.heappop(self.mn_hp)
            heapq.heappush(self.mx_hp, -mn)
        
    def findMedian(self) -> float:
        if len(self.mn_hp) == len(self.mx_hp):
            return (self.mn_hp[0] - self.mx_hp[0]) / 2
        return self.mn_hp[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()