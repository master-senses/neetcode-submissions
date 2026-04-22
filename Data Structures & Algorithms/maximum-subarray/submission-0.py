import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = -math.inf
        max_sum = -math.inf

        for i in nums:
            curr_sum = max(i, curr_sum + i)
            max_sum = max(max_sum, curr_sum)

        return max_sum