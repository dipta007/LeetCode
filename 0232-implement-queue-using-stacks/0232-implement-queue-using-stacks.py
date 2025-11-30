class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []
        

    def push(self, x: int) -> None:
        self.a.append(x)
        
    def _transfer(self):
        while self.a:
            v = self.a.pop()
            self.b.append(v)

    def pop(self) -> int:
        if self.b:
            v = self.b.pop()
            return v
        
        self._transfer()
        v = self.b.pop()
        return v

        
    def peek(self) -> int:
        if self.b:
            return self.b[-1]
        
        self._transfer()
        return self.b[-1]
        

    def empty(self) -> bool:
        return len(self.a) == 0 and len(self.b) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()