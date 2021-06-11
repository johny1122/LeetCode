#  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
#  according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

def nums_in_box(x_ind, y_ind, board):
    nums = [board[x_ind, y_ind], board[x_ind, y_ind + 1], board[x_ind, y_ind + 2],
            board[x_ind + 1, y_ind], board[x_ind + 1, y_ind + 1], board[x_ind + 1, y_ind + 2],
            board[x_ind + 2, y_ind], board[x_ind + 2, y_ind + 1], board[x_ind + 2, y_ind + 2]]
    return set(nums)


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in board:
            if len(set(int(num) for num in row if num != '.')) != 9:
                return (False, 1)

            for x_box in range(0, 9, 3):
                for y_box in range(0, 9, 3):
                    if nums_in_box(x_box, y_box, board) != 9:
                        return (False, 2)

        for column in range(9):
            col_nums = set()
            for row in range(9):
                col_nums.add(int(board[row, column]))
            if len(col_nums) != 9:
                return (False, 3)

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
