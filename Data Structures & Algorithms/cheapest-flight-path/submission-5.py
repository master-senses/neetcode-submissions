from collections import deque
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpprices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if p + prices[s] < tmpprices[d]:
                    tmpprices[d] = p + prices[s]
            prices = tmpprices
        print(prices)
        return -1 if prices[dst] == float("inf") else prices[dst]

                    





