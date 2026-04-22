class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob1(nums):
            one, two = 0, 0
            for n in nums:
                temp = max(one + n, two)
                one = two
                two = temp
            return two
        
        return max(rob1(nums[:len(nums) - 1]), rob1(nums[1:]))
