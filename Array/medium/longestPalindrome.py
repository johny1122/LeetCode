#  Given a string s, return the longest palindromic substring in s.

class Solution(object):

    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return s

        # dynamic programming:

        s_length = len(s)
        longest_pali = ''
        longest_length = 0
        dp = [None for _ in range(s_length)]

        for col in range(s_length):
            for row in range(col + 1):
                if col == row:  # one letter
                    dp[row] = True
                elif col == row + 1:  # two same letters
                    dp[row] = (s[col] == s[row])
                else:
                    dp[row] = (dp[row + 1] and s[col] == s[row])

                if dp[row] and (col - row + 1) > longest_length:
                    longest_length = (col - row + 1)
                    longest_pali = s[row:col + 1]

        return longest_pali


if __name__ == '__main__':
    solution = Solution()
    s = "babad"
    # s = "cbbd"
    # s = "ac"
    # s = "a"
    # s = ""

    print(solution.longestPalindrome(s))
