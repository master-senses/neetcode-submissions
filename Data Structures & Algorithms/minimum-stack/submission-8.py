import math

class MinStack:

    def __init__(self):
        self.array = []
        self.min_array = []
        

    def push(self, val: int) -> None:
        self.array.append(val)
        if len(self.min_array) == 0:
            self.min_array.append(val)
            return
        if self.min_array[-1] > val:
            self.min_array.append(val)
        else:
            self.min_array.append(self.min_array[-1])
        

    def pop(self) -> None:
        if (len(self.array) == 0):
            return
        self.array.pop(-1)
        self.min_array.pop(-1)
        
        

    def top(self) -> int:
        if (len(self.array) == 0):
            return
        return self.array[-1]
        

    def getMin(self) -> int:
        if (self.min_array == 0):
            return None
        return self.min_array[-1]

        
