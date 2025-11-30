from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.val = defaultdict(list)
        self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.val[key].append(value)
        self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        vals = self.val[key]
        times = self.time[key]

        if len(times) == 0:
            return ""
        
        import bisect
        ind = bisect.bisect_right(times, timestamp)
        ind -= 1
        if ind == -1:
            return ""
        return vals[ind]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)