class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for i in range(len(nums)):
            temp = max(two, one + nums[i])
            one = two
            two = temp
        
        return two