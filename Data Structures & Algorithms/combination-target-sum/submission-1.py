class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(path, cur_sum, i):
            if cur_sum == target:
                results.append(path[:])
                return
            if cur_sum > target:
                return
            if i >= len(nums):
                return

            path.append(nums[i])
            backtrack(path, cur_sum + nums[i], i)
            path.pop()
            backtrack(path, cur_sum, i + 1)
        
        backtrack([], 0, 0)
        return results
            
