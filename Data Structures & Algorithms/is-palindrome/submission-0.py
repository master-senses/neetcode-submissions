class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        new_s = ""
        for k in s:
            if k.isalnum():
                new_s += k.lower()
        j = len(new_s) - 1
        print(new_s)
        while j > i:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        return True