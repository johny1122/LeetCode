#  Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
#  according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

def nums_in_box(x_ind, y_ind, board):
    nums_list = []
    for row in range(x_ind, x_ind + 3):
        for column in range(y_ind, y_ind + 3):
            if board[row][column] != ".":
                nums_list.append(int(board[row][column]))

    return nums_list


def isValidSudoku_long_solution(board):
    # row check
    for row in board:
        nums_in_row = [int(num) for num in row if num != '.']
        set_nums_in_row = set(nums_in_row)
        if len(nums_in_row) != len(set_nums_in_row):
            return False

    # box check
    for x_box in range(0, 9, 3):
        for y_box in range(0, 9, 3):
            nums_in_box_list = nums_in_box(x_box, y_box, board)
            nums_in_box_set = set(nums_in_box_list)
            if len(nums_in_box_list) != len(nums_in_box_set):
                return False

    # column check
    for column in range(9):
        col_nums_list = []
        for row in range(9):
            if board[row][column] != ".":
                col_nums_list.append(int(board[row][column]))
        col_nums_set = set(col_nums_list)
        if len(col_nums_list) != len(col_nums_set):
            return False

    return True


def isValidSudoku_short_solution(board):
    seen = set()

    for row in range(9):
        for column in range(9):
            value = board[row][column]
            if value != ".":
                if (value, row) in seen or (value + value, column) in seen or (
                        value, row // 3, column // 3) in seen:
                    return False
                seen.add((value, row))
                seen.add((value + value, column))
                seen.add((value, row // 3, column // 3))
    return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return isValidSudoku_short_solution(board)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
    #                                  , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #                                  , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #                                  , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #                                  , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #                                  , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #                                  , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #                                  , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #                                  , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # should be True

    print(solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))  # should be False
