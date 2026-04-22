# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        traversal = []

        queue.append(root)
        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    level.append(node.val)
            if len(level) != 0:
                traversal.append(level)

        return traversal
        