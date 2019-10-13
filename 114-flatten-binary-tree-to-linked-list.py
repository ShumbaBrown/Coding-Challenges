# Given a binary tree, flatten it to a linked list in-place.
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.queue = []
        self.helper(root)

        for i in range(len(self.queue) - 1):
            self.queue[i].left = None
            self.queue[i].right = self.queue[i+1]
        self.queue[-1].left = None

        return root

    def helper(self, node):
        if not node:
            return
        self.queue.append(node)
        self.helper(node.left)
        self.helper(node.right)
        
