# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # first attempt #
        # nums_dict = {n: [] for n in nums}
        # for i in range(len(nums)):
        #     nums_dict[nums[i]].append(i)
        #
        # for n in nums_dict:
        #     if (target - n) == n:
        #         if len(nums_dict[n]) == 1:
        #             continue
        #         else:
        #             return nums_dict[n]
        #     elif nums_dict.get(target - n):
        #         return nums_dict[n] + nums_dict[target - n]

        nums_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [nums_dict[complement], i]
            else:
                nums_dict[num] = i
        return []


if __name__ == '__main__':
    s = Solution()
    # print(s.twoSum([2, 7, 11, 15], 9))
    # print(s.twoSum([3,2,4], 6))
    print(s.twoSum([3, 3], 6))
