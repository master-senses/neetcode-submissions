# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def traverse(self, root, traversal):
        if not root:
            return
        # if not root.left and not root.right:
        #     print(root.val)
        #     traversal.append(root)
        #     return
        self.traverse(root.left, traversal)
        traversal.append(root.val)
        self.traverse(root.right, traversal)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        trav = []
        self.traverse(root, trav)
        print(trav)
        return trav[k - 1]
        
