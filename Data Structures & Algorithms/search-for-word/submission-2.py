class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if min(r, c) < 0 or r >= row_len or c >= col_len or board[r][c] != word[i] or (r,c) in path:
                return False

            path.add((r, c))
            result = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return result

        for i in range(row_len):
            for j in range(col_len):
                if dfs(i, j, 0):
                    return True

        return False
