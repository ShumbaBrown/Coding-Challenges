# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
#
# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
#
# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.hasOne(root):
            return root
        return []

    def hasOne(self, node):

        if node == None:
            return False

        left = self.hasOne(node.left)
        right = self.hasOne(node.right)
        if not left:
            node.left = None
        if not right:
            node.right = None

        return node.val == 1 or left or right
        
