"""
[1,4,3,2], h = 9
ran = [1, 2, 3, 4]
l = 1
r = 0
mid = 0
val = 2
h = 9
count = 6
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        # ran = [i for i in range(1, max(piles) + 1)]
        l = 1
        r = max(piles)
        mid = 0
        speed = 0

        def eating_time(val, piles, h):
            count = 0
            for i in range(len(piles)):
                if count > h:
                    return False
                elif piles[i] % val != 0:
                    count += (piles[i] // val) + 1
                else:
                    count += piles[i] / val
                
            if count <= h:
                return True
            return False
        
        while l <= r:
            mid = l + (r - l) // 2
            # print(mid)
            if eating_time(mid, piles, h):
                r = mid - 1
                speed = mid
                # print(speed, l, r)
            else:
                l = mid + 1
        
        return speed
