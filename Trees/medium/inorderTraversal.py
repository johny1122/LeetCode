#  Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    values_list = []

    def inorderTraversal_helper(self, root):
        if root is None:
            return None

        self.inorderTraversal_helper(root.left)
        self.values_list.append(root.val)
        self.inorderTraversal_helper(root.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.values_list = []
        self.inorderTraversal_helper(root)
        return self.values_list


if __name__ == '__main__':
    solution = Solution()

    # root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    # root = TreeNode(1, TreeNode(2), None)
    root = TreeNode(1, None, TreeNode(2))
    # root = TreeNode(None)

    print(solution.inorderTraversal(root))
