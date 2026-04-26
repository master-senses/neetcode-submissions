class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # print(matrix)
        length = len(matrix)
        col_matrix = []
        for i in range(length):
            col = []
            for j in range(length):
                col.append(matrix[j][i])
            col_matrix.append(col)
            col = []
        print(col_matrix)
        
        for i in range(length):
            matrix[i] = col_matrix[i][::-1]
            # print(matrix[i])
        # print(matrix)
        # return matrix
                
        

        
