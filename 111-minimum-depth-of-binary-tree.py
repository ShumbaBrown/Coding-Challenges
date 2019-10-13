# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.depths = list()
        self.getDepths(root, 1)

        return min(self.depths)

    def getDepths(self, node, depth):
        if not node:
            return
        if node.left != None:
            self.getDepths(node.left, depth+1)
        if node.right != None:
            self.getDepths(node.right, depth+1)

        if node.left == None and node.right == None:
            self.depths.append(depth)
