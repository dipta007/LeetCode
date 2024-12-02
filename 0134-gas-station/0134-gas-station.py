class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas = gas + gas
        cost = cost + cost

        curr = 0
        l = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]

            curr += gain

            if curr < 0:
                l = i+1
                curr = 0
            
            if i - l + 1 == len(gas) // 2:
                return l
        
        return -1