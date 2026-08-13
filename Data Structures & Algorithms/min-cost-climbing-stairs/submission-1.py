"""
Input: cost = [1,2,3]

Output: 2
dp = [1, 2, 4]
dp[i] = 3 + (1) = 4

Input: cost = [1,2,1,2,1,1,1]

Output: 4
dp = [1, 2, 2, 4, 3, 4, 4]
i = 4
dp[i] = 1 + min(3, 4)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])