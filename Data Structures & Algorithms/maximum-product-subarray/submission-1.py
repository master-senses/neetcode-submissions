import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        minnum, maxnum = 1,1

        for i in nums:
            if i == 0:
                minnum, maxnum = 1,1
                continue
            tmp = maxnum * i
            maxnum = max(tmp, minnum * i, i)
            minnum = min(tmp, minnum * i, i)
            res = max(res, maxnum)
    
        return res