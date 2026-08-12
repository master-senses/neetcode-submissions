"""
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
mid = 0
l = 1, r = 0
target = 15
matrix[mid][-1] = 40
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def finalize_row(l, r, target):
            while l <= r:
                mid = (l + r) // 2
                if matrix[mid][-1] < target:
                    l = mid + 1
                elif matrix[mid][-1] > target:
                    if matrix[mid][0] > target:
                        r = mid - 1
                    else:
                        return mid
                else:
                    return mid
            return -1
        
        def search_row(row, target):
            if row[-1] == target or row[0] == target:
                return True
            l, r = 0, len(row) - 1

            while l <= r:
                mid = (l + r) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        row = finalize_row(0, len(matrix) - 1, target)
        if row == -1:
            return False
        return search_row(matrix[row], target)


