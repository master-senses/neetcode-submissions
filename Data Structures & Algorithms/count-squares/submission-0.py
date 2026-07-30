from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # x, y = points
        self.pts[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for (x, y), count in self.pts.items():
            if (abs(px - x) != abs(py - y)) or (px == x) or (y == py):
                continue
            if (px, y) in self.pts and (x, py) in self.pts:
                res += count * self.pts[(px, y)] * self.pts[(x, py)]
        
        return res
            
        
