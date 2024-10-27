class Solution:
    def maximumSwap(self, num: int) -> int:
        last_seen = {}
        num = str(num)
        num = [c for c in num]
        for i, c in enumerate(num):
            last_seen[c] = i

        for i in range(len(num)):
            c = num[i]
            for j in range(9, int(c), -1):
                js = str(j)
                if js in last_seen and last_seen[js] > i:
                    num[i], num[last_seen[js]] = num[last_seen[js]], num[i]
                    return int("".join(num))
        
        return int("".join(num))
