import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []  # store negatives
        self.minheap = []  # store positives

    def addNum(self, num: int) -> None:
        # Step 1: push to maxheap
        heapq.heappush(self.maxheap, -num)

        # Step 2: balance order (largest left -> right)
        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

        # Step 3: balance size
        if len(self.maxheap) > len(self.minheap) + 1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

        if len(self.minheap) > len(self.maxheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0]) / 2
