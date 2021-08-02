#  Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        indexes_from_end = k % length
        if length > 1 and k > 0:
            nums[:] = nums[-indexes_from_end:] + nums[: -indexes_from_end]


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))  # should return [5,6,7,1,2,3,4]
    print(solution.rotate([-1, -100, 3, 99], 2))      # should return [3,99,-1,-100]
