class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # visited = set()
        rowlen = len(board)
        collen = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= rowlen or j < 0 or j >= collen or board[i][j] == "X" or board[i][j] == "T":
                return
            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return

        def isvalid(i, j):
            if i == 0 or (i == rowlen - 1) or j == 0 or (j == collen  - 1):
                return True
            return False
        
        for i in range(rowlen):
            for j in range(collen):
                if isvalid(i, j):
                    dfs(i, j)
        # print(visited)
        for i in range(rowlen):
            for j in range(collen):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
                
    