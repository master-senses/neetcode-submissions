class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        new_array = []
        new_array.append(tokens[0])
        new_array.append(tokens[1])
        i = 1
        j = 2
        while j < len(tokens):
            if tokens[j] == "+":
                new_array[i-1] = int(new_array[i - 1]) + int(new_array[i])
                new_array.pop(i)
                i -= 1
            elif tokens[j] == "*":
                new_array[i-1] = int(new_array[i - 1]) * int(new_array[i])
                new_array.pop(i)
                i -= 1
            elif tokens[j] == "/":
                new_array[i-1] = int(int(new_array[i - 1]) / int(new_array[i]))
                new_array.pop(i)
                i -= 1
            elif tokens[j] == "-":
                new_array[i-1] = int(new_array[i - 1]) - int(new_array[i])
                new_array.pop(i)
                i -= 1
            else:
                new_array.append(tokens[j])
                i += 1
            j += 1
        return new_array[0]