#  Write a function that reverses a string. The input string is given as an array of characters s.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length // 2):
            s[i], s[length - i - 1] = s[length - i - 1], s[i]
        return s

        # cheaty solution: s.reverse()


if __name__ == '__main__':
    solution = Solution()
    # print(solution.reverseString(["h", "e", "l", "l", "o"]))      # should be ['o', 'l', 'l', 'e', 'h']
    # print(solution.reverseString(["H", "a", "n", "n", "a", "h"])) # should be ['h', 'a', 'n', 'n', 'a', 'H']
    # print(solution.reverseString(["a", "b"]))                     # should be ['b', 'a']
    print(solution.reverseString(["a"]))                            # should be ['a']
