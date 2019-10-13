#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.s_nodes = list()
        self.getNodes(s)

        for nodes in self.s_nodes:
            if self.isEqual(nodes, t):
                return True
        return False

    def getNodes(self, node):
        if not node:
            return
        self.s_nodes.append(node)
        self.getNodes(node.left)
        self.getNodes(node.right)

    def isEqual(self, node, t):
        if node == None and t == None:
            return True
        if node == None or t == None or node.val != t.val:
            return False
        return self.isEqual(node.left, t.left) and self.isEqual(node.right, t.right)
