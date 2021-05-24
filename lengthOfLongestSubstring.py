# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        longest = 0
        substr = 0
        for start_i in range(len(s)):
            for i in range(start_i, len(s)):
                if s[i] in chars:
                    break
                substr += 1
                chars[s[i]] = 0

            if substr > longest:
                longest = substr
            if substr == len(s):
                return substr
            chars = {}
            substr = 0

        return longest


if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring("abcdew"))
    # print(s.lengthOfLongestSubstring("abcd"))
    # print(s.lengthOfLongestSubstring("bbbbb"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
    # print(s.lengthOfLongestSubstring("a"))
    # print(s.lengthOfLongestSubstring(" "))
    # print(s.lengthOfLongestSubstring("aab"))
    print(s.lengthOfLongestSubstring("a bc3 4f"))
