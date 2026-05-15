class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        pq = []
        res = []

        for i in count.values():
            heapq.heappush(pq, -i)
        
        for i in range(k):
            val = -heapq.heappop(pq)
            for j in count:
                if count[j] == val:
                    res.append(j)
                    count[j] = -1
        
        return res
