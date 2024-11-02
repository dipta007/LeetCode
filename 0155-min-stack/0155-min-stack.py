class MinStack:

    def __init__(self):
        self.mn = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mn) == 0 or self.mn[-1] >= val:
            self.mn.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mn[-1]:
            self.mn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()