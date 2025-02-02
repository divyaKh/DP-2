"""
bottom up approach. TC = O(N*M) where N= length of coins array and M = amount value. SC= O(N*M)
"""

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0:
            return 0
        dp = [[0 for x in range(0, amount+1)] for x in range(0, len(coins)+1)]
        for i in range(0, len(coins)+1):
            dp[i][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j < coins[i-1]:  #amount left < current coin value
                    dp[i][j] = dp[i-1][j]   #not choosing
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]] #choosing and not choosing
        return dp[-1][-1]