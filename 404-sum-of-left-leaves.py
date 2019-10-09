# Question:
# Find the sum of all left leaves in a given binary tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
            :type root: TreeNode
            :rtype: int
            """
        if root == None:
            return 0
        right_stack = []
        left_stack = []
        if root.right != None:
            right_stack.append(root.right)
        if root.left != None:
            left_stack.append(root.left)
        total = 0
        
        while (len(right_stack) != 0 or len(left_stack) != 0):
            if (len(left_stack) != 0):
                left = left_stack.pop()
                if left.left == None and left.right == None:
                    total += left.val
                else:
                    if (left.left != None):
                        left_stack.append(left.left)
                    if (left.right != None):
                        right_stack.append(left.right)
            if (len(right_stack) != 0):
                right = right_stack.pop()
                if (right.left != None):
                    left_stack.append(right.left)
                if (right.right != None):
                    right_stack.append(right.right)
        
    return total
