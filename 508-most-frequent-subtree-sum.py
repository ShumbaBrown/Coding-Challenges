# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return list()

        self.sums = collections.Counter()
        self.findSums(root)
        ans = list()
        mostFreq = max(self.sums.values())

        for key, val in self.sums.items():
            if val == mostFreq:
                ans.append(key)

        return ans

    def findSums(self, node):
        if not node:
            return 0
        total = node.val + self.findSums(node.left) + self.findSums(node.right)
        self.sums[total] += 1
        return total
