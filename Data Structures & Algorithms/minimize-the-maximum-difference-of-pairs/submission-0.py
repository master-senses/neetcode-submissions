class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        res = nums[-1] - nums[0]

        def isValid(diff):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if p == cnt:
                    return True
            return False

        while l <= r:
            m = l + ((r - l) // 2)
            if isValid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res