class MyHashMap:

    def __init__(self):
        self.value = []

    def resize(self, key):
        if key >= len(self.value):
            self.value = self.value + [-1] * (key + 1 - len(self.value))

    def put(self, key: int, value: int) -> None:
        self.resize(key)
        self.value[key] = value

    def get(self, key: int) -> int:
        if key >= len(self.value):
            return -1
        return self.value[key]

    def remove(self, key: int) -> None:
        if key >= len(self.value): return
        self.value[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)