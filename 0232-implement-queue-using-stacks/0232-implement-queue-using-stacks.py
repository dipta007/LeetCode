class MyQueue:

    def __init__(self):
        self.buffer = []
        self.queue = []

    def push(self, x: int) -> None:
        self.buffer.append(x)
        

    def pop(self) -> int:
        if len(self.queue) == 0:
            while self.buffer:
                self.queue.append(self.buffer[-1])
                self.buffer.pop()
        tmp = self.queue.pop()
        return tmp
        

    def peek(self) -> int:
        if len(self.queue) == 0:
            while self.buffer:
                self.queue.append(self.buffer[-1])
                self.buffer.pop()
        return self.queue[-1]
        

    def empty(self) -> bool:
        return (len(self.buffer) == 0 and len(self.queue) == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()