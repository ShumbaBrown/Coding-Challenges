#Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
#Calling next() will return the next smallest number in the BST.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    
    
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

def __init__(self, root):
    """
        :type root: TreeNode
        """
            self.stack = list()
            self.pushAll(root)

        def next(self):
        """
            @return the next smallest number
            :rtype: int
            """
        tmp = self.stack.pop()
        self.pushAll(tmp.right)
                return tmp.val


def hasNext(self):
    """
        @return whether we have a next smallest number
        :rtype: bool
        """
            if len(self.stack) > 0:
                return True
                    return False

def pushAll(self, node):
    while node is not None:
        self.stack.append(node)
        node = node.left



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
