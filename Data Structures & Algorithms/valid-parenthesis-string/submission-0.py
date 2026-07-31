import math
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        ((**)
        one star can be a ")". so valid

        (((*)
        cannot match "(" with ")"

        *)
        """
        star = []
        left = []
        #  right = []

        for i in range(len(s)):
            if s[i] == "*":
                star.append(i)
            elif s[i] == "(":
                left.append(i)
            else:
                if len(left) != 0:
                    left.pop()
                elif len(star) != 0:
                    star.pop()
                else:
                    return False
        
        while left and star:
            if left.pop() > star.pop():
                return False
            
        return not left



