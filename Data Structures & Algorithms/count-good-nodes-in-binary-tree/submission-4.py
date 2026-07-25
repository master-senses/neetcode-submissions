# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we do left->right->curr traversal
        # if the curr node is greater than the max node in that traversal
        # then that node is valid
        # we take that as max and continue
        self.nodes = 0

        def traversal(max_val, curr):
            if not curr:
                return
            traversal(max(max_val, curr.val), curr.left)
            traversal(max(max_val, curr.val), curr.right)
            if curr.val < max_val:
                return
            self.nodes += 1
        
        traversal(-math.inf, root)
        return self.nodes

        #example
        """
        [2,1,1,3,null,1,5]
        root = 2
        nodes = 2
        max_val = 2
        curr = 2
        """
            