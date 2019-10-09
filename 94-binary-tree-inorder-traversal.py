#Given a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
            :type root: TreeNode
            :rtype: List[int]
            """
        self.stack = list()
        output = list()
        self.pushAllLeft(root)
        
        while len(self.stack) > 0:
            node = self.stack.pop()
            self.pushAllLeft(node.right)
            output.append(node.val)
        return output
    
    def pushAllLeft(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left
