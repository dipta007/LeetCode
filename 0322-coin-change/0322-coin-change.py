class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [100000000] * (amount + 4)

        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        return dp[amount] if dp[amount] != 100000000 else -1