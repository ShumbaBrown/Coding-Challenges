# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.isValidBSTHelper(root)

    def isValidBSTHelper(self, node, lower = float('-inf'), upper = float('inf')):
        """
        :type node: TreeNode
        :rtype: bool
        """

        if not node:
            return True

        val = node.val

        if val <= lower or val >= upper:
            return False

        if not self.isValidBSTHelper(node.left, lower, val):
            return False
        if not self.isValidBSTHelper(node.right, val, upper):
            return False
        return True









        # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
            :type root: TreeNode
            :rtype: bool
            """

        return self.isValidBSTHelper(root, float('-inf'), float('inf'))

    def isValidBSTHelper(self, root, lower, upper):
        """
            :type root: TreeNode
            :rtype: bool
            """

        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if root.left != None and root.right != None:
            if root.left.val <= lower or root.right.val >= upper or root.left.val >= root.val or root.val >= root.right.val:
                return False
            return self.isValidBSTHelper(root.left, lower, root.val) and self.isValidBSTHelper(root.right, root.val, upper)
        if root.left != None:
            if root.left.val <= lower or root.left.val >= root.val:
                return False
            return self.isValidBSTHelper(root.left, lower, root.val)
        if root.right != None:
            if root.right.val >= upper or root.val >= root.right.val:
                return False
            return self.isValidBSTHelper(root.right, root.val, upper)
