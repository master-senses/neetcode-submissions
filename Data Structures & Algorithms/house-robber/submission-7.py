class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 2:
            return max(nums[0], nums[1])
        amount = [0] * len(nums)
        amount[0], amount[1] = nums[0], nums[1]
        for i in range(2, len(nums)):
            amount[i] = max(amount[i - 1], nums[i] + max(amount[0:i - 1]))
            print(nums, amount)

        return amount[len(nums) - 1]