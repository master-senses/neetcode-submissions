import math

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # rows = set()
        # cols = set()
        ROW_LEN = len(matrix)
        COL_LEN = len(matrix[0])

        def replace_row(row):
            for i in range(COL_LEN):
                if matrix[row][i] != 0:
                    matrix[row][i] = math.inf

        def replace_col(col):
            for i in range(ROW_LEN):
                if matrix[i][col] != 0:
                    matrix[i][col] = math.inf
            
        
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                if matrix[row][col] == 0:
                    replace_row(row)
                    replace_col(col)
        
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                if matrix[row][col] == math.inf:
                    matrix[row][col] = 0
        



        