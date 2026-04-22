from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_array = []
        counter = Counter(nums)
        if counter[0] == 0:
            prod = 1
            for i in nums:
                prod *= i
            
            for j in range(len(nums)):
                prod_array.append(int(prod / nums[j]))

            # return prod_array
        elif counter[0] >= 2:
            return [0] * len(nums)
        else:
            zero_index = -1
            prod = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    zero_index = i
                else:
                    prod *= nums[i]
            prod_array = [0] * len(nums)
            prod_array[zero_index] = prod
        
        return prod_array


        