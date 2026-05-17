class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [-1] * (n + 1)
        print(output)
        # output[0] = 1
        for i in range(n + 1):
            count = 0
            # print(i)
            num = i
            while num:
                if output[num] != -1:
                    count += output[num]
                    break
                if num & 1:
                    count += 1
                num = num >> 1
            # print(output[i])
            output[i] = count
            # print(output)
        
        return output