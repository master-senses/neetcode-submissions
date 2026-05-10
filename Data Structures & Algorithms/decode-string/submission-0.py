class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def helper() -> str:
            res = ""
            num = 0
            while self.i < len(s):
                if s[self.i].isalpha():
                    res += s[self.i]
                elif s[self.i] == "]":
                    return res
                elif s[self.i].isdigit():
                    num = num*10 + int(s[self.i])
                elif s[self.i] == "[":
                    self.i += 1
                    res += int(num) * helper()
                    num = 0
                self.i += 1
            return res
        
        res = helper()
        return res



