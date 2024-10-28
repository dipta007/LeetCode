class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def call(total):
            if total == 0:
                return 0
            
            if total < 0:
                return 1000000
            
            res = 1000000
            for c in coins:
                res = min(res, 1 + call(total - c))

            return res
        
        res = call(amount)
        return res if res != 1000000 else -1