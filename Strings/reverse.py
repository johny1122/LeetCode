# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value
# to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

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
