class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) / 2
        dp = set()
        dp.add(0)

        for n in nums:
            numset = set()
            for t in dp:
                if t + n == target:
                    return True
                numset.add(t)
                numset.add(t + n)
            dp = numset
        
        return False


