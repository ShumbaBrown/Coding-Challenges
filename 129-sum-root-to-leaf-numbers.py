#Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
#An example is the root-to-leaf path 1->2->3 which represents the number 123.
##Find the total sum of all root-to-leaf numbers.
##Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
            :type root: TreeNode
            :rtype: int
            """
        
        return (self.sumNumbersHelper(root, 0))
    
    def sumNumbersHelper(self, root, path):
        if (root == None):
            return path
        total = 0
        
        # If leaf node, bubble up path
        if (root.left == None and root.right == None):
            return (path*10 + root.val)
        
        if (root.left != None):
            total += self.sumNumbersHelper(root.left, (path*10 + root.val))
        if (root.right != None):
            total += self.sumNumbersHelper(root.right, (path*10 + root.val))
        
        return total

