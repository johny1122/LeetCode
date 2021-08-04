#  Given a string s, find the length of the longest substring without repeating characters.

from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Brute Force:

        # longest_sub = 0
        # len_s = len(s)
        # for index in range(len_s):
        #     letters_dict = defaultdict(int)
        #     cur_sub = 0
        #     for i in range(index, len_s):
        #         if letters_dict[s[i]] == 1:
        #             break
        #         letters_dict[s[i]] = 1
        #         cur_sub += 1
        #
        #     if cur_sub > longest_sub:
        #         longest_sub = cur_sub
        #
        # return longest_sub
        # ============================================
        # Sliding window:

        start, longest_sub = 0, 0
        len_s = len(s)
        letters_dict = defaultdict(int)

        for end in range(len_s):
            if s[end] in letters_dict:
                start = max(start, letters_dict[s[end]])

            longest_sub = max(longest_sub, end - start + 1)
            letters_dict[s[end]] = end + 1

        return longest_sub


if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"
    # s = "abba"

    print(solution.lengthOfLongestSubstring(s))
