class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        final_array = []
        for i in range(len(nums)):
            if sorted_nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            if i and sorted_nums[i] == sorted_nums[i - 1]:
                # print(l)
                continue
            while l < r:   
                triplet_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if triplet_sum > 0:
                    r -= 1
                elif triplet_sum < 0:
                    l += 1
                else:
                    final_array.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1

        return final_array
