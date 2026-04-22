class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
            print(l, mid, r)
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[r]:
                if target >= nums[mid]:
                    l = mid + 1
                else:
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
        
        return -1
        