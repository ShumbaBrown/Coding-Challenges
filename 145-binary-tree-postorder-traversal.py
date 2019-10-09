# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.stack = list()
        output = list()
        seen = dict()

        self.pushAllLeft(root)

        while len(self.stack) > 0:
            node = self.stack.pop()
            if node.val not in seen:
                seen[node.val] = True
                if node.right != None:
                    self.stack.append(node)
                    self.pushAllLeft(node.right)
                else:
                    output.append(node.val)
            else:
                output.append(node.val)
        return output




    def pushAllLeft(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left
