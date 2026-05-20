# stream is not sorted
# numbers can be negative
# can be duplicate numbers, just have to get middle index
# for even, it's mean of 2 middle values, for odd just middle value
# median can be decimal

# min_h = [-1] 
# max_h = [1, -1]
import heapq
class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_h, num)

        if self.max_h and -self.max_h[0] > self.min_h[0]:
            val = heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, -val)


        if len(self.min_h) > len(self.max_h) + 1:
            val = heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, -val)

        if len(self.max_h) > len(self.min_h):
            val = -heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, val)
        
        
    def findMedian(self) -> float:
        if (len(self.min_h) + len(self.max_h)) % 2 != 0:
            return self.min_h[0]
        else:
            return (-self.max_h[0] + self.min_h[0]) / 2
        