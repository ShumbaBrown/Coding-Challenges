# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #in order add to list then print list at index k
        self.values = list()
        self.createList(root)

        return self.values[k-1]

    def createList(self, node):
        if not node:
            return

        self.createList(node.left)
        self.values.append(node.val)
        self.createList(node.right)
