from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1, len(nums) + 1))
        return list(all_nums - set(nums))


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(s.findDisappearedNumbers([1, 1]))
