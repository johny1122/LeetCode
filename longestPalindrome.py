# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        elif s[0] == s[-1]:
            if len(s) == 2:
                return s
            return s[0] + self.longestPalindrome(s[1:-1]) + s[-1]

        else:
            longest_left = self.longestPalindrome(s[:-1])
            longest_right = self.longestPalindrome(s[1:])
            return longest_left if len(longest_left) >= len(longest_right) else longest_right


if __name__ == '__main__':
    s = Solution()
    # print(s.longestPalindrome("babad"))
    # print(s.longestPalindrome("cabab"))
    # print(s.longestPalindrome("cbbd"))
    # print(s.longestPalindrome("a"))
    # print(s.longestPalindrome("ac"))
    # print(s.longestPalindrome("acA"))
    # print(s.longestPalindrome("ac1a1"))
    # print(s.longestPalindrome("1a1"))
    print(s.longestPalindrome("aaba"))  # not working
