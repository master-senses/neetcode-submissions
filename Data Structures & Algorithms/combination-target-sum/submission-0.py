class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(path, i, sums):
            if sums == target:
                result.append(path[:])
                return
            if i >= len(nums) or sums > target:
                return
            path.append(nums[i])
            backtracking(path, i, sums + nums[i])
            path.pop()
            backtracking(path, i + 1, sums)

        backtracking([], 0, 0)
        return result
                

            

            
            
