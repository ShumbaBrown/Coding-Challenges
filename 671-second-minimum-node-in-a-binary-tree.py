# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.values = set()
        self.dfs(root)

        if len(self.values) < 2:
            return -1

        for i in range(2):
            smallest = None
            for each in self.values:
                if smallest == None or each < smallest:
                    smallest = each
            self.values.remove(smallest)
        return smallest

    def dfs(self, node):
        if node:
            self.values.add(node.val)
            self.dfs(node.left)
            self.dfs(node.right)


        
