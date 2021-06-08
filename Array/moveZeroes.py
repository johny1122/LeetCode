#  Given an integer array nums, move all 0's to the end of it while maintaining the relative order
#  of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
        return nums


if __name__ == '__main__':
    solution = Solution()
    # print(solution.moveZeroes([0, 1, 0, 3, 12]))
    print(solution.moveZeroes([0]))
