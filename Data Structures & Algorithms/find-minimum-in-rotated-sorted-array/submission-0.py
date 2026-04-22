import math
class Solution:

    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            else:
                minimum = min(minimum, nums[mid])
                if nums[mid] >= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return minimum