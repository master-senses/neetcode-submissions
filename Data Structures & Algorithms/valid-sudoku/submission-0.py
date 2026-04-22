class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                # defining a box
                box = []
                print(col)
                start = 0
                if col == 0:
                    start = col - 3
                row1 = board[row][col: col + 3]
                row2 = board[row + 1][col: col + 3]
                row3 = board[row + 2][col: col + 3]
                for i in range(3):
                    box.append(row1[i])
                    box.append(row2[i])
                    box.append(row3[i])
                print(box)
                dupl = Counter(box)
                for i in dupl:
                    if i != "." and dupl[i] > 1:
                        return False

        for col in range(9):
            column = []
            for row in range(9):
                column.append(board[row][col])
            # print(column)
            dupl = Counter(column)
            for i in dupl:
                if i != "." and dupl[i] > 1:
                    return False

        for row in range(9):
            print(board[row])
            dupl = Counter(board[row])
            for i in dupl:
                    if i != "." and dupl[i] > 1:
                        return False
        return True
