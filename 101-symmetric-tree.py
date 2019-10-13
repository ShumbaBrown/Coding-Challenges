# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    def isMirror(self, left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            return (left.val == right.val) and self.isMirror(left.right, right.left) and self.isMirror(right.left, left.right)

            
