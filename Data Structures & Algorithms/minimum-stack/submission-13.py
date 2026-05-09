import math
import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        # heapq.heapify(self.min_stack)
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) > 0:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        return
        

    def pop(self) -> None:
        value = self.stack[-1]
        self.stack.pop(-1)
        self.min_stack.pop(-1)
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
