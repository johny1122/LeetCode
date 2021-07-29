# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Definition for a binary tree node.

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        level_list = []
        queue = deque()
        queue.append(root)

        while queue:
            level_nodes = [node for node in queue]  # nodes of new level

            level_values = []
            for node in level_nodes:  # save the level's values
                if node is not None:
                    level_values.append(node.val)

            level_list.append(level_values)  # insert new level to solution
            queue.clear()

            for node in level_nodes:  # insert children of current level for next iteration
                if node is None:
                    continue
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            if not queue:  # if all children are None -> exit
                break

        return level_list


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3, TreeNode(9, None, None),
                    TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    # root = TreeNode(1, None, None)
    # root = None

    print(solution.levelOrder(root))
