class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = [-math.inf] * (len(nums) + 1)
        # summ = -math.inf
        for i in range(len(nums)):
            res[i + 1] = max(res[i] + nums[i], nums[i])
        
        return max(res)
            