#  Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
#  (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this
# character in if it is either. This determines if the final result is negative or positive respectively.
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached.
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read,
# then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer
# so that it remains in the range. Specifically, integers less than -231 should be clamped to -231,
# and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

import re


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        match_value = re.search('( *)(\+|-|)(\d*).*', s)
        max_limit = 2 ** 31 - 1
        min_limit = -2 ** 31
        if match_value is not None:
            if (match_value.group(3) is not None) and (match_value.group(3) != ''):
                num = int(match_value.group(3))
                if match_value.group(2) == '-':
                    num = -num
                if num <= min_limit:
                    return min_limit
                if num >= max_limit:
                    return max_limit
                return num
            return 0
        return 0


if __name__ == '__main__':
    solution = Solution()
    # print(solution.myAtoi("42"))
    # print(solution.myAtoi("4193 with words"))
    # print(solution.myAtoi("words and 987"))
    # print(solution.myAtoi("-91283472332"))
    # print(solution.myAtoi("aaa-91283472332"))
    # print(solution.myAtoi("aaa 333"))
    print(solution.myAtoi("+-12"))
