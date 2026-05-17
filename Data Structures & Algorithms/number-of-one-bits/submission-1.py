class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # integer = n % 10
        # print(integer)
        # rem = n // 10
        # print(rem)
        # print(n >> 1)
        # print(n >> 1)
        while n != 0:
            if n & 1:
                count += 1
            n = n >> 1
            # integer = n % 10
            # rem = rem // 10
        
        return count