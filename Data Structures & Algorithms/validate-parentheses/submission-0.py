class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack) == 0 or i == "(" or i == "[" or i == "{":
                stack.append(i)    
            elif i == ")":
                elem = stack.pop()
                if elem != "(":
                    return False
            elif i == "]":
                elem = stack.pop()
                if elem != "[":
                    return False
            elif i == "}":
                elem = stack.pop()
                if elem != "{":
                    return False
        if len(stack) == 0:
            return True
        return False
        