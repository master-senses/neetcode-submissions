# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        stack = deque()
        visited = set()
        stack.append(root)
        # values.append(root.val)

        while stack:
            node = stack.pop()
            # print(node.val)
            if node not in visited and node:
                visited.add(node)
                stack.append(node.left)
                stack.append(node.right)
                values.append(node.val)
                print(values)
        print(values)
        sorted_vals = sorted(values)
        return sorted_vals[k - 1]