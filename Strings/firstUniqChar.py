# Given a string s, return the first non-repeating character in it and return its index.
# If it does not exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_dict = {}

        for i in range(len(s)):
            if s[i] not in count_dict:
                count_dict[s[i]] = (i, 1)
            else:
                count_dict[s[i]] = (count_dict[s[i]][0], count_dict[s[i]][1] + 1)

        for i in range(len(s)):
            if count_dict[s[i]][1] == 1:
                return count_dict[s[i]][0]

        return -1  # not found one
    
        # another solution:
        #       letters = 'abcdefghijklmnopqrstuvwxyz'
        #       index = [s.index(l) for l in letters if s.count(l) == 1]
        #       return min(index) if len(index)>0 else -1

if __name__ == '__main__':
    solution = Solution()
    # print(solution.firstUniqChar("leetcode"))
    # print(solution.firstUniqChar("loveleetcode"))
    # print(solution.firstUniqChar("aabb"))
    print(solution.firstUniqChar(""))