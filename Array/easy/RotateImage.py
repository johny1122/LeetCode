#  You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range((n % 2) + (n // 2)):
            for j in range(n // 2):
                save_temp = matrix[j][i]
                matrix[j][i] = matrix[n - 1 - i][j]
                matrix[n - 1 - i][j] = matrix[n - 1 - j][n - 1 - i]
                matrix[n - 1 - j][n - 1 - i] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = save_temp
        return matrix


if __name__ == '__main__':
    solution = Solution()
    # print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    # print(solution.rotate([[1]]))
    print(solution.rotate([[1,2],[3,4]]))
