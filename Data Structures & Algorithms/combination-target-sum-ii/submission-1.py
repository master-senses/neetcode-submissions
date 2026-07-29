from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [1,2,3,4,5], target = 7
        Counter = {1: 1, 2 : 1, 3: 1, 4: 1, 5: 1}

        """
        # self.count = Counter(candidates)
        output = []
        candidates.sort()
        def dfs(i, total, comb):
            if total == target:
                output.append(comb[:])
                return
            if total > target or i == len(candidates):
                return
            
            # use i
            comb.append(candidates[i])
            dfs(i + 1, total + candidates[i], comb)
            # remove i
            comb.pop()
            while (i + 1 < len(candidates)) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total, comb)
        
        dfs(0, 0, [])
        
        return output
        

            