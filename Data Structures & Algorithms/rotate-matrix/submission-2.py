class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # print(matrix)
        length = len(matrix)
        # col_matrix = []÷
        for i in range(length):
            for j in range(i + 1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(col_matrix)
        
        for i in range(length):
            matrix[i] = matrix[i][::-1]
            # print(matrix[i])
        # print(matrix)
        # return matrix
                
        

        
