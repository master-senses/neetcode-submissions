# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        visited = set()
        level_order = []

        queue.append(root)
        # level_order.append([root.val])
        while queue:
            # node = queue.pop(0)
            q_len = len(queue)
            level = []
            for i in range(q_len):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                level_order.append(level)

        return level_order


        