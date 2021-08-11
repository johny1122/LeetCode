#  Given an integer array nums where the elements are sorted in ascending order, convert it
#  to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of
# every node never differs by more than one.
#
#

from levelOrder import Solution as solution_of_levelOrder

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == '__main__':
    solution = Solution()
    list = [-10,-3,0,5,9]
    # list = [1,3]
    print(solution_of_levelOrder().levelOrder(solution.sortedArrayToBST(list)))