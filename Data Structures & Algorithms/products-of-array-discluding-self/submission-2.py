from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        prod_array = [1] * count
        frwrd = 1
        # forward pass
        for i in range(count):
            prod_array[i] = frwrd
            frwrd *= nums[i]

        #back pass
        back = 1
        for j in range(count - 1, -1, -1):
            prod_array[j] *= back
            back *= nums[j]

        return prod_array
            

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # length = len(nums)
        # res = [1] * length

        # prefix = 1
        # for i in range(length):
        #     res[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(length - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]

        # return res


        