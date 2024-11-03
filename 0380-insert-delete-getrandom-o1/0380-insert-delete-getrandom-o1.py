class RandomizedSet:

    def __init__(self):
        self.values = []
        self.v_to_i = {}

    def insert(self, val: int) -> bool:
        # print(self.values, self.v_to_i)
        if val in self.v_to_i and self.v_to_i[val] != -1:
            return False
        self.v_to_i[val] = len(self.values)
        self.values.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.v_to_i or self.v_to_i[val] == -1:
            return False
        
        ind = self.v_to_i[val]
        
        self.v_to_i[val] = -1
        if ind != len(self.values) - 1:
            self.v_to_i[self.values[-1]] = ind

        self.values[ind], self.values[-1] = self.values[-1], self.values[ind]
        self.values.pop()

        # print("r", val, self.values, self.v_to_i)
        return True

    def getRandom(self) -> int:
        import random
        ind = random.randint(0, len(self.values)-1)
        return self.values[ind]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()