# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root1, root2):
            if (not root1 and root2) or (root1 and not root2):
                return False
            if not root1 and not root2:
                return True
            if root1.val != root2.val:
                return False
            # print(root1.val, root2.val)
            
            return compare(root1.left, root2.left) and compare(root1.right, root2.right)
        
        def search(root, subRoot):
            if not root:
                return False
            if not subRoot:
                return True
            if root.val == subRoot.val:
                # print(root.val, subRoot.val)
                # print(compare(root, subRoot))
                if compare(root, subRoot):
                    return True
            # print(root.val)
            return search(root.left, subRoot) or search(root.right, subRoot)
            # return False
        
        return search(root, subRoot)
        
            
            
            
            
