#  Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]

        return dic.values()

# longer solution:
        # if len(strs) == 1:
        #     return [strs]
        # dict_by_length = {}
        # dict_by_anagram = {}
        #
        # for word in strs:
        #     word_len = len(word)
        #     if not dict_by_length.get(word_len):
        #         anagram_dict = defaultdict(int)
        #         for letter in word:
        #             anagram_dict[letter] += 1
        #         dict_by_length[word_len] = [(word, anagram_dict)]
        #         dict_by_anagram[word] = [word]
        #
        #     else:
        #         letter_count = defaultdict(int)
        #         for letter in word:
        #             letter_count[letter] += 1
        #
        #         found_anagram = False
        #         for value in dict_by_length.get(word_len):
        #             anagram = value[0]
        #             same_anagram = True
        #             for letter in letter_count:
        #                 if (letter not in anagram) or (letter_count[letter] > value[1][letter]):
        #                     same_anagram = False
        #                     break
        #
        #             if same_anagram:
        #                 dict_by_anagram[anagram].append(word)
        #                 found_anagram = True
        #                 break
        #
        #         if not found_anagram:
        #             dict_by_anagram[word] = [word]
        #             dict_by_length[word_len].append((word, letter_count))
        #
        # return dict_by_anagram.values()





if __name__ == '__main__':
    solution = Solution()

    strs = ["eat","tea","tan","ate","nat","bat"]
    # strs = ["evil", "santa", "vile", "listen", "satan", "silent"]
    # strs = ["ddddddddddg","dgggggggggg"]
    # strs = [""]
    # strs = ["a"]
    print(solution.groupAnagrams(strs))