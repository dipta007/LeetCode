from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[], []]
        
        self.map[key][0].append(timestamp)
        self.map[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        ind = bisect_right(self.map[key][0], timestamp) - 1
        if ind == -1:
            return ""
        return self.map[key][1][ind]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)