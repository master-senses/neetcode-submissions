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
        # dp = [0] * len(cost)
        first = cost[0]
        second = cost[1]
        curr = 0

        for i in range(2, len(cost)):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        
        return min(first, second)