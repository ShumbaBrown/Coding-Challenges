# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.traversal = list()
        self.helper(root, 0)
        return self.traversal[::-1]

    def helper(self, node, depth):

        if not node:
            return

        if len(self.traversal) < depth+1:
            self.traversal.append(list())
        self.traversal[depth].append(node.val)
        if node.left != None:
            self.helper(node.left, depth+1)
        if node.right != None:
            self.helper(node.right, depth+1)

        
