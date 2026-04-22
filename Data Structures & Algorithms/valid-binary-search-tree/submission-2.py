# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, maxi, mini):
            if not node:
                return True
            
            if mini < node.val < maxi:
                return valid(node.left, node.val, mini) and valid(node.right, maxi, node.val)
            
            return False
        
        return valid(root, math.inf, -math.inf)

        
        

        
