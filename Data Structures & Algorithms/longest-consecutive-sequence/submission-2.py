class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        main_count = 0
        numbers = {}

        for i in nums:
            numbers[i] = False
        
        for i in nums:
            if not numbers[i]:
                local_count = 0
                while i in numbers:
                    i += 1
                    local_count += 1
                main_count = max(main_count, local_count)
        return main_count

            