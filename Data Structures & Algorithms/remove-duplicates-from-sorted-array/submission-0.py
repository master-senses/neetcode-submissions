class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        a = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[a] = nums[i]
                a += 1
                k += 1
        
        return k