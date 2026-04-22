# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = []
        visited = set()
        queue.append(root)
        string = []

        while queue:
            node = queue.pop(0)
            # print(node)
            if node not in visited:
                if node:
                    string.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    string += "n"
        # print(string)
        return ",".join(string)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        if data == "":
            return None
        nodes = data.split(",")
        queue = []
        root = TreeNode(nodes[0])
        queue.append(root)
        index = 0
        while queue:
            node = queue.pop(0)
            # print(nodes[index + 1])
            if nodes[index + 1] != "n":
                node.left = TreeNode(int(nodes[index + 1]))
                queue.append(node.left)
                # index += 1
            if nodes[index + 2] != "n":
                node.right = TreeNode(int(nodes[index + 2]))
                queue.append(node.right)
                # index += 1
            index += 2

        return root
