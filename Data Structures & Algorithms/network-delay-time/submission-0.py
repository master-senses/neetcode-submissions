from heapq import heapify, heappush, heappop
import math

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        dist = {}
        for node1, node2, time in times:
            if node1 not in adj:
                adj[node1] = []
            if node2 not in adj:
                adj[node2] = []
            adj[node1].append((time, node2))
        
        for i in range(1, n + 1):
            if i == k:
                dist[k] = 0
            else:
                dist[i] = math.inf
        
        heap = [(0, k)]
        heapify(heap)

        while heap:
            t, node = heappop(heap)

            if t > dist[node]:
                continue
            
            neighbours = adj[node]
            for time, nei in neighbours:
                new_dist = time + dist[node]
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heappush(heap, (dist[nei], nei))
        
        return max(dist.values()) if max(dist.values()) != math.inf else -1

"""
adj = {
1: [(1, 2), (4, 4)],
2: [1, 3],
3: [(1, 4)],
4: []
}
dist = {
1: 0
2: inf
3: inf
4: inf
}
heap = [(1, 2), (4, 4)]
neighbours = [(1, 2), (4, 4)]
time = 1, nei = 2
new_dist = 1 + 0 = 1
"""


        