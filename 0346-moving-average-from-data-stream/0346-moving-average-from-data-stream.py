from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.cum = 0
        self.dq = deque()

    def next(self, val: int) -> float:
        self.cum += val
        self.dq.append(val)
        while len(self.dq) > self.size:
            v = self.dq.popleft()
            self.cum -= v
        return self.cum / len(self.dq)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)