class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rowlen = len(board)
        collen = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= rowlen or j < 0 or j >= collen:
                return
            if board[i][j] == "X":
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return
        
        # for col in range(collen):
        #     if board[0][col] == "O":
        #         dfs(0, col)
        
        # for col in range(collen):
        #     if board[rowlen - 1][col] == "O":
        #         dfs(rowlen - 1, col)
        
        # for row in range(rowlen):
        #     if board[row][0] == "O":
        #         dfs(row, 0)
        
        # for row in range(rowlen):
        #     if board[row][collen - 1] == "O":
        #         dfs(row, collen - 1)
        def isvalid(i, j):
            if i == 0 or (i == rowlen - 1) or j == 0 or (j == collen  - 1):
                return True
            return False
        
        for i in range(rowlen):
            for j in range(collen):
                if isvalid(i, j):
                    dfs(i, j)
        print(visited)
        for i in range(rowlen):
            for j in range(collen):
                # print(board[i][j] == "O")
                if board[i][j] == "O" and (i, j) not in visited:
                    # print(i, j)
                    board[i][j] = "X"
                    # print(board[i][j])
        # print(board)
    