from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        freq = Counter(hand)
        groups = []
        length = int(len(hand) % groupSize)
        for i in range(length):
            groups.append([])
        heap = list(freq.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]
            for i in range(first, first + groupSize):
                if i not in freq:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)



        
        return True
        # [1, 2, 2, 3, 3, 4, 4, 5]

