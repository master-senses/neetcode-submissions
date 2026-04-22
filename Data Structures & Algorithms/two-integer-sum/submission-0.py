class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            if nums[i] in diff:
                return [diff[nums[i]][0], i]
            elif (target - nums[i]) in diff:
                diff[target - nums[i]].append(i)
            else:
                diff[target - nums[i]] = [i]

        return [0,0]
        