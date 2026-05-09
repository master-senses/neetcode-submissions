import math
import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        heapq.heapify(self.min_stack)
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.min_stack, val)
        return
        

    def pop(self) -> None:
        value = self.stack[-1]
        self.stack.pop(-1)
        self.min_stack.remove(value)
        heapq.heapify(self.min_stack)
        return

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[0]
        
