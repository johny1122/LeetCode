from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        all_nums = {}
        for element in nums:
            if element not in all_nums:
                all_nums[element] = 1
            else:
                all_nums[element] += 1

        for value in all_nums.values():
            if value >= 2:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
    print(s.containsDuplicate([1, 2, 3, 4]))
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
