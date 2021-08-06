#  Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
#  that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        sol = []
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            temp_target = 0 - nums[i]

            while left < right:
                left_right_sum = nums[left] + nums[right]
                if left_right_sum > temp_target:
                    right -= 1
                elif left_right_sum < temp_target:
                    left += 1
                else:
                    arr = [nums[i], nums[left], nums[right]]
                    sol.append(arr)

                    while left < right and nums[left] == arr[1]:
                        left += 1
                    while left < right and nums[right] == arr[2]:
                        right -= 1

        return sol


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0]
    # nums = []
    print(solution.threeSum(nums))
