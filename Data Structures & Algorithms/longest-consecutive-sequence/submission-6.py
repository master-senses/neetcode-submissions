class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        main_count = 0
        numbers = {}

        for i in nums:
            numbers[i] = False
        
        for i in nums:
            if i - 1 not in numbers:
                local_count = 0
                j = i
                while j in numbers:
                    numbers[j] = True
                    j += 1
                    local_count += 1
                numbers[i] = True
                main_count = max(main_count, local_count)
        return main_count

            