class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = len(nums)
        if count == 0 or count == 1:
            return count
        checked = set()
        longest = 1
        for i in nums:
            length = 1
            if i not in checked:
                checked.add(i)
                j = i - 1
                while j in set(nums):
                    length += 1
                    if length > longest:
                        longest = length
                    j -= 1
        return longest
        