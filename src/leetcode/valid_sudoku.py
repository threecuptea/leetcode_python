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
        def box(r, c):
            return r // 3 * 3 + c // 3
        # key is row num, col num and box num .  The same number can appear in the same row or col or box twice
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                # if that number has already appeared in the current row, col or box
                b = box(r, c)
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[b].add(val)
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