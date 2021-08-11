#  Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
import math


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    prev = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.prev is not None and self.prev >= root.val:
            return False

        self.prev = root.val
        if not self.isValidBST(root.right):
            return False

        return True


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    # root = TreeNode(5, TreeNode(1, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None)))
    # root = TreeNode(1, None, None)
    # root = None
    print(solution.isValidBST(root))
