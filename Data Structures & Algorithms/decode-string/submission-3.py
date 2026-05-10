class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        # num = 0

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack[-1] + substr
                    stack.pop()
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack[-1] + k
                    stack.pop()
                substr = int(k) * substr
                stack.append(substr)
        return "".join(stack)

            


