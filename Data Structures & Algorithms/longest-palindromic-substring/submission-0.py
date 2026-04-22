class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = ""

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print(len(length), (r - l + 1))
                if len(length) < (r - l + 1):
                    length = ""
                    length = s[l:r + 1]
                    print("odd ", length)
                l -= 1
                r += 1
                
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(length) < (r - l + 1):
                    length = ""
                    length = s[l:r + 1]
                    print("even", length)
                l -= 1
                r += 1
                

        return length