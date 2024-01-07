class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache
        def call(ind):
            if ind >= len(days):
                return 0
            
            res = 100000000000
            for c, d in zip(costs, [1, 7, 30]):
                dd = days[ind] + d - 1
                for i in range(ind, len(days)):
                    if days[i] <= dd:
                        res = min(res, c + call(i+1))
            return res
        
        return call(0)
