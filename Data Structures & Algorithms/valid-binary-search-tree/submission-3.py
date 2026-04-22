# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root, maxi, mini):
            if not root:
                return True
            if mini < root.val < maxi:
                return isvalid(root.left, root.val, mini) and isvalid(root.right, maxi, root.val)
            else:
                return False
            return True
        
        return isvalid(root, math.inf, -math.inf)

        
        

        
