class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l + ((r - l) // 2)] == target:
                return l + ((r - l) // 2)
            elif nums[l + ((r - l) // 2)] > target:
                r = l + ((r - l) // 2) - 1
            else:
                l = l + ((r - l) // 2) + 1
        
        return -1