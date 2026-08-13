"""
1) cannot have a leading 0
2) 12 has multiple ways to decode (1, 2 / 12)
3)A->Z represents 1->26, 27 only has one way to decode (2, 7)

1012 -> (JAB, JAL)
1212 -> (1 21 2), (12, 1, 2), (1, 2, 12), (1, 2, 1, 2), (12, 12)
121 -> 1, 21 / 12, 1 / 1, 2, 1
12121 -> (1,2 , 1, 2, 1) / (12, 1, 2, 1) / (1, 2, 12, 1) / (12, 12, 1) / (1, 2, 1, 21) / (12, 1, 21) / (1, 21, 21) / (1, 21, 2, 1)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i < (len(s) - 1)) and ((s[i] == "1") or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)


        