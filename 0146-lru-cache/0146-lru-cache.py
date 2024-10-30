from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.count = {}
        self.elems = set()
        self.value = {}
        self.dq = deque()
        self.cap = capacity

    def get(self, key: int) -> int:
        tmp = self.value.get(key, -1)
        if tmp != -1:
            self.count[key] += 1
            self.dq.append(key)
        return tmp

    def put(self, key: int, value: int) -> None:
        self.elems.add(key)
        self.value[key] = value
        self.dq.append(key)
        self.count[key] = self.count.get(key, 0) + 1
        while len(self.elems) > self.cap:
            v = self.dq.popleft()
            self.count[v] -= 1
            if self.count[v] == 0:
                self.elems.remove(v)
                self.value[v] = -1
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)