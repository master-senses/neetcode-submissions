class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        ROW_LEN = len(matrix)
        COL_LEN = len(matrix[0])

        def replace_row(row):
            # if row in rows:
            #     return
            # rows.add(row)
            for i in range(COL_LEN):
                matrix[row][i] = 0

        def replace_col(col):
            # if col in cols:
            #     return
            # cols.add(col)
            for i in range(ROW_LEN):
                matrix[i][col] = 0
            
        
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                if matrix[row][col] == 0:
                    rows.add(row)
                    cols.add(col)
        
        for row in rows:
            print(row)
            replace_row(row)
        
        for col in cols:
            replace_col(col)
        
        # return matrix



        