#  Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the
#  result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_count = {}

        for num in nums1:
            if num in dict_count:
                dict_count[num] += 1
            else:
                dict_count[num] = 1

        result = []
        for num in nums2:
            if num in dict_count and dict_count[num] > 0:
                result.append(num)
                dict_count[num] -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.intersect([1,2,2,1], [2,2]))           # should return [2,2]
    # print(solution.intersect([4,9,5], [9,4,9,8,4]))       # should return [4,9]
    print(solution.intersect([4,9,5], [9,4,5,9,8,4]))     # should return [4,9,5]


