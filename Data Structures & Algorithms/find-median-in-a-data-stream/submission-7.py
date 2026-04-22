import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        heapq.heapify(self.maxheap)
        self.minheap = []
        heapq.heapify(self.minheap)

    def addNum(self, num: int) -> None:
        maxlen = len(self.maxheap)
        minlen = len(self.minheap)

        if maxlen == 0:
            heapq.heappush(self.maxheap, -num)
            return

        if minlen == 0:
            if num < -self.maxheap[0]:
                val = -heapq.heappop(self.maxheap)
                heapq.heappush(self.maxheap, -num)
                heapq.heappush(self.minheap, val)
            else:
                heapq.heappush(self.minheap, num)
            return

        if maxlen >= minlen:
            if num < -self.maxheap[0]:
                heapq.heappush(self.maxheap, -num)
                val = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, val)
            else:
                heapq.heappush(self.minheap, num)
            return

        if minlen > maxlen:
            if num > self.minheap[0]:
                heapq.heappush(self.minheap, num)
                val = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -val)
            else:
                heapq.heappush(self.maxheap, -num)
            return

    def findMedian(self) -> float:
        maxlen = len(self.maxheap)
        minlen = len(self.minheap)

        if (maxlen + minlen) % 2 != 0:
            if maxlen > minlen:
                return -self.maxheap[0]
            else:
                return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2
