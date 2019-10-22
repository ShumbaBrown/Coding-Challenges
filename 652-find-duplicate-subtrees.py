# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node values.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.count = collections.Counter()
        self.ans = list()

        self.serialize(root)
        return self.ans

    def serialize(self, node):
        if not node:
            return "#"
        serial = "{},{},{}".format(node.val, self.serialize(node.left), self.serialize(node.right))
        self.count[serial] += 1
        if self.count[serial] == 2:
            self.ans.append(node)
        return serial
