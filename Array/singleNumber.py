#  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 2, 1]))                     # should return 1
    print(solution.singleNumber([4, 1, 2, 1, 2]))               # should return 4
    print(solution.singleNumber([2]))                           # should return 2
    print(solution.singleNumber([1, 5, 2, 3, 5, 6, 3, 2, 6]))   # should return 1
