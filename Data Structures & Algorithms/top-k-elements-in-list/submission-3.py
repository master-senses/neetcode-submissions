class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        pq = []
        res = []

        for i in count:
            heapq.heappush(pq, (count[i], i))
            if len(pq) > k:
                heapq.heappop(pq)

        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res
