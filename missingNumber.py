from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = {num: None for num in nums}
        for i in range(len(nums) + 1):
            if i not in all_nums:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
    print(s.missingNumber([0, 1]))
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
