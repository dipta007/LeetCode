class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(jewels)
        cnt = 0
        for s in stones:
            cnt += int(s in j)
        return cnt