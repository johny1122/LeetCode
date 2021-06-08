#  Given a non-empty array of decimal digits representing a non-negative
#  integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each
# element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        if digits[0] < 9:
            digits[0] += 1
        else:
            digits[0] = 0
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    solution = Solution()
    # print(solution.plusOne([1, 2, 3]))         # should return [1,2,4]
    # print(solution.plusOne([4, 3, 2, 1]))      # should return [4,3,2,2]
    # print(solution.plusOne([0]))               # should return [1]
    print(solution.plusOne([9,9,9]))             # should return [1,0,0,0]
