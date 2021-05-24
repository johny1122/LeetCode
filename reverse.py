# https://leetcode.com/problems/reverse-integer/
import math


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        negative = False
        if x < 0:
            negative = True
            x = abs(x)

        while x != 0:
            result *= 10
            result += x % 10
            x = int(x / 10)
        if result > math.pow(2, 31) - 1:
            return 0
        return result if not negative else -result


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
