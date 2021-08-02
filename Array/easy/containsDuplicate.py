# Given an integer array nums, return true if any value appears at least twice in the array, and return
# false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_count = {}

        for num in nums:
            if dict_count.get(num):
                dict_count[num] += 1
            else:
                dict_count[num] = 1

        for key in dict_count:
            if dict_count[key] > 1:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    # print(solution.containsDuplicate([1, 2, 3, 1]))                    # should return True
    # print(solution.containsDuplicate([1, 2, 3, 4]))                    # should return False
    # print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))    # should return True
    print(solution.containsDuplicate([1]))  # should return True
