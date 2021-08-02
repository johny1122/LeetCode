#  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two
#  integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside
# the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements
# denote the elements that should be merged, and the last n elements are set to 0 and should be
# ignored. nums2 has a length of n.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        for i in range(1, m + 1):
            nums1[-i], nums1[m - i] = nums1[m - i], nums1[-i]

        r_index, m_index, n_index = 0, n, 0
        while m_index < m + n and n_index < n:
            if nums1[m_index] <= nums2[n_index]:
                nums1[r_index] = nums1[m_index]
                m_index += 1
            else:
                nums1[r_index] = nums2[n_index]
                n_index += 1

            r_index += 1

        while m_index < m + n:
            nums1[r_index] = nums1[m_index]
            m_index += 1
            r_index += 1

        while n_index < n:
            nums1[r_index] = nums2[n_index]
            n_index += 1
            r_index += 1


if __name__ == '__main__':
    solution = Solution()

    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3

    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5

    # nums1 = [4,5,6,0,0,0]
    # m = 3
    # nums2 = [1,2,3]
    # n = 3

    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1

    solution.merge(nums1, m, nums2, n)
    print(nums1)
