from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW_LEN = len(grid)
        COL_LEN = len(grid[0])
        INF = 2147483647
        q = deque()
        ranges = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q):
            # global grid
            # depth = 0
            visited = set()

            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    # visited.add((row, col))
                    for dr, dc in ranges:
                        rown, coln = row + dr, col + dc
                        if rown < 0 or coln < 0 or rown >= ROW_LEN or coln >= COL_LEN or grid[rown][coln] != INF:
                            continue
                        q.append((rown, coln))
                        # visited.add((rown, coln))
                        grid[rown][coln] = grid[row][col] + 1
                # depth += 1



            
        
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                # print(grid[row][col])
                if grid[row][col] == 0:
                    # print("hi")
                    q.append((row, col))
        
        bfs(q)
                