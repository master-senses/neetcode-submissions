class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, num in enumerate(nums):
            # print(num)
            if num in diff:
                return [diff[num], i]
            else:
                diff[target - num] = i
        
        return [0, 0]

        