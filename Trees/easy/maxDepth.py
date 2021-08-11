#  Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth_helper(self, node):
        if node.left is None and node.right is None:
            return 1
        max_right, max_left = 0, 0
        if node.left is not None:
            max_left = self.maxDepth_helper(node.left) + 1
        if node.right is not None:
            max_right = self.maxDepth_helper(node.right) + 1

        return max_left if max_left > max_right else max_right

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.maxDepth_helper(root)


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    # root = TreeNode(1, TreeNode(9, None, None),
    #                 TreeNode(20, TreeNode(15, TreeNode(10, TreeNode(9, None, None), None), None), TreeNode(7, None, None)))
    # root = TreeNode(1, TreeNode(9, None, None), TreeNode(7, None, None))
    # root = TreeNode(1, None, None)
    # root = None
    print(solution.maxDepth(root))
