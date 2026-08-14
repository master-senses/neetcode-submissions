"""
res = [d, e, f]
temp = [dg, dh, di]
digit = 4
curr = e
letter = 

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        rel = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        output = [""]
        # temp = []
        for digit in digits:
            # num = int(digits[i])
            temp = []
            for curr in output:
                for letter in rel[digit]:
                    temp.append(curr + letter)
            output = temp

        return output if digits else []



    


        
