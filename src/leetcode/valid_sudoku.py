from typing import List
from collections import defaultdict
###############
# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/
# Determine if a 9 x 9 Sudoku board is valid.
# Each row, column or box must contain the digits 1-9 without repetition.
# #############
class Solution:
    # row_idx, col_idx, box_idx are all keyed by the Sudoku number.
    # Values are all row indexes, and column indexes for col_idx etc.
    # I can check if there is existing row index 0 for Sudoku number 3, ex.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The formula to get box number.
        def get_box_num(r, c):
            return (r // 3) * 3 + c // 3 # r

        row_idx, col_idx, box_idx = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(0, 9):
            for col in range(0, 9):
                val = board[row][col]
                if not val.isdigit():
                    continue
                box = get_box_num(row, col)
                # defaultdict will return empty set and no need to protect
                if row in row_idx[val] or col in col_idx[val] or box in box_idx[val]:
                    return False
                row_idx[val].add(row)
                col_idx[val].add(col)
                box_idx[val].add(box)
        return True

def main():
    board =[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    print(f'Input= {board}')
    solution = Solution()
    print(f'Output= {solution.isValidSudoku(board)}')

if __name__ == "__main__":
    main()